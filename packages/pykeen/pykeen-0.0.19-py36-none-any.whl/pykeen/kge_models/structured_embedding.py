# -*- coding: utf-8 -*-

"""Implementation of structured model (SE)."""

import logging

import numpy as np
import torch
import torch.autograd
from torch import nn

from pykeen.constants import SE_NAME, SCORING_FUNCTION_NORM, NORM_FOR_NORMALIZATION_OF_ENTITIES
from .base import BaseModule
from .trans_e import TransEConfig

__all__ = ['StructuredEmbedding']

log = logging.getLogger(__name__)


class StructuredEmbedding(BaseModule):
    """An implementation of Structured Embedding (SE) [bordes2011]_.

    This model projects different matrices for each relation head and tail entity.

    .. [bordes2011] Bordes, A., *et al.* (2011). `Learning Structured Embeddings of Knowledge Bases
                    <http://www.aaai.org/ocs/index.php/AAAI/AAAI11/paper/download/3659/3898>`_. AAAI. Vol. 6. No. 1.
    """

    model_name = SE_NAME
    margin_ranking_loss_size_average: bool = True
    hyper_params = BaseModule.hyper_params + [SCORING_FUNCTION_NORM, NORM_FOR_NORMALIZATION_OF_ENTITIES]

    def __init__(self, config):
        super().__init__(config)
        config = TransEConfig.from_dict(config)

        # Embeddings
        self.l_p_norm_entities = config.lp_norm
        self.scoring_fct_norm = config.scoring_function_norm

        self.m_left_rel_embeddings = nn.Embedding(self.num_relations, self.embedding_dim * self.embedding_dim)
        self.m_right_rel_embeddings = nn.Embedding(self.num_relations, self.embedding_dim * self.embedding_dim)

        self._initialize()

    def _initialize(self):
        entity_embeddings_init_bound = m_left_relation_embeddings_init_bound = 6 / np.sqrt(self.embedding_dim)
        nn.init.uniform_(
            self.entity_embeddings.weight.data,
            a=-entity_embeddings_init_bound,
            b=entity_embeddings_init_bound,
        )
        nn.init.uniform_(
            self.m_left_rel_embeddings.weight.data,
            a=-m_left_relation_embeddings_init_bound,
            b=m_left_relation_embeddings_init_bound,
        )

        norms = torch.norm(self.m_left_rel_embeddings.weight, p=2, dim=1).data
        self.m_left_rel_embeddings.weight.data = self.m_left_rel_embeddings.weight.data.div(
            norms.view(self.num_relations, 1).expand_as(self.m_left_rel_embeddings.weight))

    def _compute_loss(self, pos_scores, neg_scores):
        """

        :param pos_scores:
        :param neg_scores:
        :return:
        """
        y = np.repeat([-1], repeats=pos_scores.shape[0])
        y = torch.tensor(y, dtype=torch.float, device=self.device)

        # Scores for the psotive and negative triples
        pos_scores = torch.tensor(pos_scores, dtype=torch.float, device=self.device)
        neg_scores = torch.tensor(neg_scores, dtype=torch.float, device=self.device)

        loss = self.criterion(pos_scores, neg_scores, y)

        return loss

    def _compute_scores(self, projected_head_embs, projected_tail_embs):
        """

        :param h_embs:
        :param r_embs:
        :param t_embs:
        :return:
        """
        # Subtract the vector element wise
        difference = projected_head_embs - projected_tail_embs

        distances = torch.norm(difference, dim=1, p=self.scoring_fct_norm).view(size=(-1,))

        return distances

    def _project_entities(self, entity_embs, projection_matrix_embs):
        entity_embs = entity_embs.unsqueeze(-1)

        projected_entity_embs = torch.matmul(projection_matrix_embs, entity_embs)

        return projected_entity_embs

    def predict(self, triples):
        """

        :param head:
        :param relation:
        :param tail:
        :return:
        """
        # triples = torch.tensor(triples, dtype=torch.long, device=self.device)
        heads = triples[:, 0:1]
        relations = triples[:, 1:2]
        tails = triples[:, 2:3]

        head_embs = self.entity_embeddings(heads).view(-1, self.embedding_dim)
        tail_embs = self.entity_embeddings(tails).view(-1, self.embedding_dim)

        m_left_r_embs = self.m_left_rel_embeddings(relations).view(-1, self.embedding_dim, self.embedding_dim)
        m_right_r_embs = self.m_right_rel_embeddings(relations).view(-1, self.embedding_dim, self.embedding_dim)

        projected_head_embs = self._project_entities(entity_embs=head_embs,
                                                     projection_matrix_embs=m_left_r_embs)
        projected_tails_embs = self._project_entities(entity_embs=tail_embs,
                                                      projection_matrix_embs=m_right_r_embs)

        scores = self._compute_scores(projected_head_embs=projected_head_embs,
                                      projected_tail_embs=projected_tails_embs)

        return scores.detach().cpu().numpy()

    def forward(self, batch_positives, batch_negatives):
        """

        :param batch_positives:
        :param batch_negatives:
        :return:
        """
        # Normalise embeddings of entities
        norms = torch.norm(self.entity_embeddings.weight, p=self.l_p_norm_entities, dim=1).data
        self.entity_embeddings.weight.data = self.entity_embeddings.weight.data.div(
            norms.view(self.num_entities, 1).expand_as(self.entity_embeddings.weight))

        pos_heads = batch_positives[:, 0:1]
        pos_relations = batch_positives[:, 1:2]
        pos_tails = batch_positives[:, 2:3]

        neg_heads = batch_negatives[:, 0:1]
        neg_relations = batch_negatives[:, 1:2]
        neg_tails = batch_negatives[:, 2:3]

        pos_h_embs = self.entity_embeddings(pos_heads).view(-1, self.embedding_dim)
        pos_m_left_r_embs = self.m_left_rel_embeddings(pos_relations).view(-1, self.embedding_dim, self.embedding_dim)
        pos_m_right_r_embs = self.m_right_rel_embeddings(pos_relations).view(-1, self.embedding_dim, self.embedding_dim)

        pos_t_embs = self.entity_embeddings(pos_tails).view(-1, self.embedding_dim)

        neg_h_embs = self.entity_embeddings(neg_heads).view(-1, self.embedding_dim)
        neg_m_left_r_embs = self.m_left_rel_embeddings(neg_relations).view(-1, self.embedding_dim, self.embedding_dim)
        neg_m_right_r_embs = self.m_right_rel_embeddings(neg_relations).view(-1, self.embedding_dim, self.embedding_dim)
        neg_t_embs = self.entity_embeddings(neg_tails).view(-1, self.embedding_dim)

        projected_pos_head_embs = self._project_entities(entity_embs=pos_h_embs,
                                                         projection_matrix_embs=pos_m_left_r_embs)
        projected_pos_tails_embs = self._project_entities(entity_embs=pos_t_embs,
                                                          projection_matrix_embs=pos_m_right_r_embs)

        projected_neg_head_embs = self._project_entities(entity_embs=neg_h_embs,
                                                         projection_matrix_embs=neg_m_left_r_embs)
        projected_neg_tails_embs = self._project_entities(entity_embs=neg_t_embs,
                                                          projection_matrix_embs=neg_m_right_r_embs)

        pos_scores = self._compute_scores(projected_head_embs=projected_pos_head_embs,
                                          projected_tail_embs=projected_pos_tails_embs)

        neg_scores = self._compute_scores(projected_head_embs=projected_neg_head_embs,
                                          projected_tail_embs=projected_neg_tails_embs)

        loss = self._compute_loss(pos_scores=pos_scores, neg_scores=neg_scores)

        return loss
