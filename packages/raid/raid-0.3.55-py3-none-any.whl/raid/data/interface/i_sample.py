# -*- coding: utf-8 -*-

"""
A single piece of data. This interface must be implemented.
* By default all samples must have a list of discrete labels.
* These labels must be integers.
* It must be able to return a one-hot tensor for these labels.
* It must include a mapping to semantic names.
* Can be extended for regression based problems or single-label problems.
"""

import torch
from typing import List, Dict

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class ISample:

    def __init__(self, id: str, labels: List[int], label_map: Dict[int, str]):
        self.id: str = id  # ID of the sample.
        self.labels: List[int] = labels
        self.label_map: Dict[int, str] = label_map  # Mapping the index to semantic label
        self.n_classes: int = len(self.label_map)

    def __str__(self):
        return f"<Sample {self.id} | L: {self.labels}>"

    def __repr__(self):
        return str(self)

    @property
    def semantic_labels(self):
        semantic_labels = [self.label_map[i] for i in self.labels]
        return semantic_labels

    @property
    def label_tensor(self):
        return torch.Tensor(self.labels)

    @property
    def one_hot_tensor(self):
        one_hot_array = [0] * self.n_classes
        for i in self.labels:
            one_hot_array[i] = 1
        return torch.Tensor(one_hot_array)
