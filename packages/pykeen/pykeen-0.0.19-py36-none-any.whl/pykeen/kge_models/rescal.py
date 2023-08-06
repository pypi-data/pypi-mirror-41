# -*- coding: utf-8 -*-

"""Implementation of RESCAL."""

import numpy as np
import torch
import torch.autograd
from torch import nn

from pykeen.constants import RESCAL_NAME, SCORING_FUNCTION_NORM
from pykeen.kge_models.base import BaseModule

__all__ = ['RESCAL']


class RESCAL(BaseModule):
    """An implementation of RESCAL [nickel2011]_.

    This model represents relations as matrices and models interactions between latent features.

    .. [nickel2011] Nickel, M., *et al.* (2011) `A Three-Way Model for Collective Learning on Multi-Relational Data
                    <http://www.cip.ifi.lmu.de/~nickel/data/slides-icml2011.pdf>`_. ICML. Vol. 11.
    """

    model_name = RESCAL_NAME
    margin_ranking_loss_size_average: bool = True
    hyper_params = BaseModule.hyper_params + [SCORING_FUNCTION_NORM]

    def __init__(self, config):
        super().__init__(config)

        # Embeddings
        self.relation_embeddings = nn.Embedding(self.num_relations, self.embedding_dim * self.embedding_dim)

        self.scoring_fct_norm = config[SCORING_FUNCTION_NORM]

    def _compute_loss(self, pos_scores, neg_scores):
        # TODO: Check
        y = np.repeat([-1], repeats=pos_scores.shape[0])
        y = torch.tensor(y, dtype=torch.float, device=self.device)

        # Scores for the psotive and negative triples
        pos_scores = torch.tensor(pos_scores, dtype=torch.float, device=self.device)
        neg_scores = torch.tensor(neg_scores, dtype=torch.float, device=self.device)
        # neg_scores_temp = 1 * torch.tensor(neg_scores, dtype=torch.float, device=self.device)

        loss = self.criterion(pos_scores, neg_scores, y)

        return loss

    def _compute_scores(self, h_embs, r_embs, t_embs):
        """

        :param h_embs:
        :param r_embs:
        :param t_embs:
        :return:
        """
        # Compute score and transform result to 1D tensor
        M = r_embs.view(-1, self.embedding_dim, self.embedding_dim)
        h_embs = h_embs.unsqueeze(-1).permute([0, 2, 1])
        h_M_embs = torch.matmul(h_embs, M)
        t_embs = t_embs.unsqueeze(-1)
        scores = -torch.matmul(h_M_embs, t_embs).view(-1)

        # scores = torch.bmm(torch.transpose(h_emb, 1, 2), M)  # h^T M
        # scores = torch.bmm(scores, t_emb)  # (h^T M) h
        # scores = score.view(-1, 1)

        return scores

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
        relation_embs = self.relation_embeddings(relations).view(-1, self.embedding_dim)
        tail_embs = self.entity_embeddings(tails).view(-1, self.embedding_dim)

        scores = self._compute_scores(h_embs=head_embs, r_embs=relation_embs, t_embs=tail_embs)

        return scores.detach().cpu().numpy()

    def forward(self, batch_positives, batch_negatives):
        """

        :param batch_positives:
        :param batch_negatives:
        :return:
        """

        pos_heads = batch_positives[:, 0:1]
        pos_relations = batch_positives[:, 1:2]
        pos_tails = batch_positives[:, 2:3]

        neg_heads = batch_negatives[:, 0:1]
        neg_relations = batch_negatives[:, 1:2]
        neg_tails = batch_negatives[:, 2:3]

        pos_h_embs = self.entity_embeddings(pos_heads).view(-1, self.embedding_dim)
        pos_r_embs = self.relation_embeddings(pos_relations).view(-1, self.embedding_dim)
        pos_t_embs = self.entity_embeddings(pos_tails).view(-1, self.embedding_dim)

        neg_h_embs = self.entity_embeddings(neg_heads).view(-1, self.embedding_dim)
        neg_r_embs = self.relation_embeddings(neg_relations).view(-1, self.embedding_dim)
        neg_t_embs = self.entity_embeddings(neg_tails).view(-1, self.embedding_dim)

        pos_scores = self._compute_scores(h_embs=pos_h_embs, r_embs=pos_r_embs, t_embs=pos_t_embs)
        neg_scores = self._compute_scores(h_embs=neg_h_embs, r_embs=neg_r_embs, t_embs=neg_t_embs)

        loss = self._compute_loss(pos_scores=pos_scores, neg_scores=neg_scores)

        return loss
