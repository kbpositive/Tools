import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import imageio
import os


class Piece:
    def __init__(self, row, col, board):
        self.pos = np.array([row, col])
        self.rewards = board

    def state(self):
        return self.pos - (np.array([len(self.rewards), len(self.rewards[0])]) / 2.0)

    def reward(self):
        return self.rewards[self.pos[0]][self.pos[1]]


class King(Piece):
    moves = {
        0: np.array([-1, -1]),
        1: np.array([-1, 0]),
        2: np.array([-1, 1]),
        3: np.array([0, -1]),
        4: np.array([0, 0]),
        5: np.array([0, 1]),
        6: np.array([1, -1]),
        7: np.array([1, 0]),
        8: np.array([1, 1]),
    }

    def move(self, n):

        return self


class Knight(Piece):
    pass


r = np.zeros((8, 8))
k = King(0, 0, r)

print(k.state())
print(k.reward())
