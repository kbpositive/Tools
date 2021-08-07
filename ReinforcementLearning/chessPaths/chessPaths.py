import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import imageio
import os


class Board:
    def __init__(self, rewards):
        self.rewards = rewards

    def state(self, pos):
        return pos - (np.array([len(self.rewards), len(self.rewards[0])]) / 2.0)

    def reward(self, pos):
        return self.rewards[pos[0]][pos[1]]


class Piece:
    def __init__(self, pos):
        self.pos = pos

    def reinforce(self, actual, pred):
        return pred - actual * tf.math.log(pred)


class King(Piece):
    def __init__(self, rewards):
        self.moves = {
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

        self.model = models.Sequential(
            [layers.Dense(len(self.moves), input_shape=(2,), activation="softmax")]
        )
        self.optimizer = optimizers.Adam(learning_rate=0.015)
        self.model.compile(
            loss=self.reinforce, optimizer=self.optimizer, metrics="MeanAbsoluteError"
        )
        super(King, self).__init__(rewards)


class Knight(Piece):
    pass
