import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import imageio
import os


class bandit:
    def __init__(self, context, arms):
        self.arms = arms
        self.context = context
        self.actions = np.array(
            [np.random.uniform(0.0, 1.0, arms) for _ in range(context)]
        )
        self.state = np.eye(context)
        self.model = models.Sequential(
            [layers.Dense(arms, input_shape=(arms,), activation="sigmoid")]
        )
        self.optimizer = optimizers.Adam(learning_rate=0.015)
        self.model.compile(
            loss=self.reinforce, optimizer=self.optimizer, metrics="MeanAbsoluteError"
        )

    def pull(self, state):
        return np.array(
            [
                (0.0) ** int(action < np.random.uniform(0.0, 1.0))
                for action in self.actions[state]
            ]
        )

    def reinforce(self, actual, pred):
        return pred - actual * tf.math.log(pred)


if __name__ == "__main__":
    context = 4
    arms = 4
    con = bandit(context, arms)
    result = []
    files = []

    for epoch in range(100):
        con.model.fit(
            con.state,
            np.mean(
                [[con.pull(i) for i in range(len(con.actions))] for _ in range(1000)],
                axis=0,
            ),
            epochs=1,
            verbose=0,
        )
        result.append(np.mean(con.model.predict(con.state) - con.actions, axis=0))
        fig, axs = plt.subplots(ncols=2)
        sns.lineplot(
            data=np.array(result),
            palette={0: "#8FCACA", 1: "#8FCACA", 2: "#8FCACA", 3: "#8FCACA"},
            dashes={0: "", 1: "", 2: "", 3: ""},
            ax=axs[0],
        )
        sns.lineplot(
            data=np.transpose(
                np.append(con.model.predict(con.state), con.actions, axis=0)
            ),
            palette={
                0: "#8FCACA",
                1: "#8FCACA",
                2: "#8FCACA",
                3: "#8FCACA",
                4: "#FFAEA5",
                5: "#FFAEA5",
                6: "#FFAEA5",
                7: "#FFAEA5",
            },
            dashes={0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            ax=axs[1],
        )

        files.append(f"./results/{epoch}.png")
        plt.savefig(files[-1])
        plt.close()

    with imageio.get_writer("./results.gif", mode="I") as writer:
        for file in files:
            image = imageio.imread(file)
            writer.append_data(image)
        for _ in range(36):
            image = imageio.imread(files[-1])
            writer.append_data(image)

    for file in set(files):
        os.remove(file)