import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class bandit:
    def __init__(self, arms):
        self.arms = arms
        self.actions = np.random.uniform(0.0, 1.0, arms)
        self.state = np.ones(arms)
        self.model = models.Sequential(
            [layers.Dense(arms, input_shape=(arms,), activation="sigmoid")]
        )
        self.optimizer = optimizers.Adam(learning_rate=0.01)
        self.model.compile(
            loss=self.reinforce, optimizer=self.optimizer, metrics="MeanAbsoluteError"
        )

    def pull(self):
        return np.array(
            [
                (0.0) ** int(action < np.random.uniform(0.0, 1.0))
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
        con.model.fit(
            np.array([con.state]),
            np.array([np.mean([con.pull() for _ in range(1000)], axis=0)]),
            epochs=1,
            verbose=0,
        )
        result.append(
            np.mean(con.model.predict(np.array([con.state]))[0] - con.actions)
        )
    sns.lineplot(data=result)
    plt.savefig("./results.png")
