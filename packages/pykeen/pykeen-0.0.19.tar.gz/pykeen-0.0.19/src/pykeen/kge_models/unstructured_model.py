# -*- coding: utf-8 -*-

"""Implementation of UM."""

import logging

import numpy as np
import torch
import torch.autograd
from torch import nn

from pykeen.constants import UM_NAME, NORM_FOR_NORMALIZATION_OF_ENTITIES, SCORING_FUNCTION_NORM
from pykeen.kge_models.base import BaseModule
from .trans_e import TransEConfig

__all__ = ['UnstructuredModel']

log = logging.getLogger(__name__)


class UnstructuredModel(BaseModule):
    """An implementation of Unstructured Model (UM) [bordes2014]_.

    .. [bordes2014] Bordes, A., *et al.* (2014). `A semantic matching energy function for learning with
                    multi-relational data <https://link.springer.com/content/pdf/10.1007%2Fs10994-013-5363-6.pdf>`_.
                    Machine
    """

    model_name = UM_NAME
    margin_ranking_loss_size_average: bool = True
    hyper_params = BaseModule.hyper_params + [SCORING_FUNCTION_NORM, NORM_FOR_NORMALIZATION_OF_ENTITIES]

    def __init__(self, config):
        super().__init__(config)
        config = TransEConfig.from_dict(config)

        self.l_p_norm_entities = config.lp_norm
        self.scoring_fct_norm = config.scoring_function_norm

        self._initialize()

    def _initialize(self):
        entity_embeddings_init_bound = 6 / np.sqrt(self.embedding_dim)
        nn.init.uniform_(
            self.entity_embeddings.weight.data,
            a=-entity_embeddings_init_bound,
            b=entity_embeddings_init_bound,
        )

    def _compute_loss(self, pos_scores, neg_scores):
        y = np.repeat([-1], repeats=pos_scores.shape[0])
        y = torch.tensor(y, dtype=torch.float, device=self.device)

        # Scores for the psotive and negative triples
        pos_scores = torch.tensor(pos_scores, dtype=torch.float, device=self.device)
        neg_scores = torch.tensor(neg_scores, dtype=torch.float, device=self.device)
        # neg_scores_temp = 1 * torch.tensor(neg_scores, dtype=torch.float, device=self.device)

        loss = self.criterion(pos_scores, neg_scores, y)

        return loss

    def _compute_scores(self, h_embs, t_embs):
        # Add the vector element wise
        sum_res = h_embs - t_embs
        distances = torch.norm(sum_res, dim=1, p=self.scoring_fct_norm).view(size=(-1,))
        distances = distances ** 2
        return distances

    def predict(self, triples):
        # triples = torch.tensor(triples, dtype=torch.long, device=self.device)
        heads = triples[:, 0:1]
        relations = triples[:, 1:2]
        tails = triples[:, 2:3]

        head_embs = self.entity_embeddings(heads).view(-1, self.embedding_dim)
        tail_embs = self.entity_embeddings(tails).view(-1, self.embedding_dim)

        scores = self._compute_scores(h_embs=head_embs, t_embs=tail_embs)

        return scores.detach().cpu().numpy()

    def forward(self, batch_positives, batch_negatives):
        # Normalize embeddings of entities
        pos_heads = batch_positives[:, 0:1]
        pos_tails = batch_positives[:, 2:3]

        neg_heads = batch_negatives[:, 0:1]
        neg_tails = batch_negatives[:, 2:3]

        pos_h_embs = self.entity_embeddings(pos_heads).view(-1, self.embedding_dim)
        pos_t_embs = self.entity_embeddings(pos_tails).view(-1, self.embedding_dim)

        neg_h_embs = self.entity_embeddings(neg_heads).view(-1, self.embedding_dim)
        neg_t_embs = self.entity_embeddings(neg_tails).view(-1, self.embedding_dim)

        pos_scores = self._compute_scores(h_embs=pos_h_embs, t_embs=pos_t_embs)
        neg_scores = self._compute_scores(h_embs=neg_h_embs, t_embs=neg_t_embs)

        loss = self._compute_loss(pos_scores=pos_scores, neg_scores=neg_scores)

        return loss
