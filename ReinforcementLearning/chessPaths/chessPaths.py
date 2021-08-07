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
        self.dims = np.array([len(self.rewards), len(self.rewards[0])])

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
        self.optimizer = optimizers.Adam(learning_rate=0.008)
        self.model.compile(
            loss=self.reinforce,
            optimizer=self.optimizer,
            metrics=tf.keras.metrics.MeanAbsoluteError(),
        )
        super(King, self).__init__(rewards)


class Knight(Piece):
    pass


if __name__ == "__main__":
    r = Board(np.zeros((8, 8)) + 0.5)
    r.rewards[-1][0] = 1.0
    r.rewards[0][-1] = 1.0
    r.rewards[0][0] = 0.0
    r.rewards[-1][-1] = 0.0

    k = King(np.array([0, 0]))

    inputs = np.array([r.state(k.pos)])
    outputs = np.array(
        [
            [
                r.reward(k.pos + move)
                if min(r.dims - np.absolute(k.pos + move)) > 0
                else r.reward(k.pos)
                for move in k.moves.values()
            ]
        ]
    )

    result = []
    files = []
    for epoch in range(10):
        history = k.model.fit(
            inputs,
            outputs,
            epochs=1,
            verbose=0,
        )

        result.append(history.history[[i for i in history.history.keys()][-1]])
        fig, axs = plt.subplots(ncols=2)
        sns.lineplot(
            data=np.array(result),
            color={0: "#8FCACA"},
            ax=axs[0],
        )
        sns.lineplot(
            data=np.append(
                k.model.predict(inputs),
                outputs,
                axis=0,
            ).T,
            palette={
                0: "#8FCACA",
                1: "#FFBEB5",
            },
            dashes={0: "", 1: ""},
            ax=axs[1],
        )

        files.append(f"./chessPaths/results/{epoch}.png")
        plt.savefig(files[-1])
        plt.close()

    with imageio.get_writer("./chessPaths/results.gif", mode="I") as writer:
        for file in files:
            image = imageio.imread(file)
            writer.append_data(image)
        for _ in range(36):
            image = imageio.imread(files[-1])
            writer.append_data(image)

    for file in set(files):
        os.remove(file)
