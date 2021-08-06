import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import tensorflow.keras.backend as kb
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython import display


class bandit:
    def __init__(self, arms):
        self.arms = arms
        self.actions = np.random.uniform(-1.0, 1.0, arms)
        self.state = np.ones(arms)
        self.model = models.Sequential(
            [layers.Dense(arms, input_shape=(arms,), activation="tanh")]
        )
        self.optimizer = optimizers.Adam(learning_rate=0.025)
        self.model.compile(loss=self.reinforce, optimizer=self.optimizer)

    def pull(self):
        return np.array(
            [
                (-1.0) ** int(action > np.random.uniform(-1.0, 1.0))
                for action in self.actions
            ]
        )

    def reinforce(self, actual, pred):
        return pred - actual * tf.math.log(pred)


if __name__ == "__main__":
    arms = 4
    con = bandit(arms)
    result = []

    for epoch in range(100):
        continue
