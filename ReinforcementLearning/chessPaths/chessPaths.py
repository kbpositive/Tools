import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import imageio
import os


class Piece:
    def __init__(self, row, col, board):
        self.pos = row, col
        self.rewards = board

    def state(self):
        return self.pos[0] - (len(self.rewards) / 2.0), self.pos[1] - (
            len(self.rewards[0]) / 2.0
        )

    def reward(self):
        return self.rewards[self.pos[0]][self.pos[1]]


class King(Piece):
    pass


class Knight(Piece):
    pass


r = np.zeros((8, 8))
k = King(0, 0, r)

print(k.state())
print(k.reward())
