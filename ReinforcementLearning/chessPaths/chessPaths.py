import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import imageio
import os


class Board:
    def __init__(self, rewards):
        self.rewards = rewards
        self.dims = np.array([len(self.rewards), len(self.rewards[0])])

    def state(self, pos):
        return np.eye(self.dims[0] * self.dims[1])[pos[0] * 8 + pos[1]]

    def reward(self, pos):
        return self.rewards[pos[0]][pos[1]]


class Piece:
    def __init__(self, pos):
        self.pos = pos
        self.discount = 0.95

    def reinforce(self, actual, pred):
        return pred - actual * tf.math.log(pred)

    def rollout(self, board, moves, state, timesteps, depth=1):
        if timesteps == 0:
            return np.array(
                [
                    board.reward(
                        state + action
                        if (
                            0 <= (state + action)[0] < board.dims[0]
                            and 0 <= (state + action)[1] < board.dims[1]
                        )
                        else state
                    )
                    for action in moves
                ]
            ) * (self.discount ** depth)

        return (
            np.array(
                [
                    board.reward(
                        state + action
                        if (
                            0 <= (state + action)[0] < board.dims[0]
                            and 0 <= (state + action)[1] < board.dims[1]
                        )
                        else state
                    )
                    + np.sum(
                        [
                            self.rollout(
                                board,
                                moves,
                                np.array(
                                    state + action
                                    if (
                                        0 <= (state + action)[0] < board.dims[0]
                                        and 0 <= (state + action)[1] < board.dims[1]
                                    )
                                    else state
                                ),
                                timesteps - 1,
                                depth + 1,
                            )
                        ]
                    )
                    / len(moves)
                    for action in moves
                ]
            )
            * (self.discount ** depth)
        )


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
            [
                layers.Dense(len(self.moves), input_shape=(64,), activation="sigmoid"),
            ]
        )
        self.optimizer = optimizers.Adam(learning_rate=0.06)
        self.model.compile(
            loss=self.reinforce,
            optimizer=self.optimizer,
            metrics=tf.keras.metrics.MeanAbsoluteError(),
        )
        super(King, self).__init__(rewards)


class Knight(Piece):
    def __init__(self, rewards):
        self.moves = {
            0: np.array([-2, -1]),
            1: np.array([-1, -2]),
            2: np.array([2, -1]),
            3: np.array([1, -2]),
            4: np.array([0, 0]),
            5: np.array([-2, 1]),
            6: np.array([-1, 2]),
            7: np.array([2, 1]),
            8: np.array([1, 2]),
        }

        self.model = models.Sequential(
            [
                layers.Dense(len(self.moves), input_shape=(64,), activation="sigmoid"),
            ]
        )
        self.optimizer = optimizers.Adam(learning_rate=0.06)
        self.model.compile(
            loss=self.reinforce,
            optimizer=self.optimizer,
            metrics=tf.keras.metrics.MeanAbsoluteError(),
        )
        super(Knight, self).__init__(rewards)


if __name__ == "__main__":
    # k = King(np.array([0, 0]))
    k = Knight(np.array([0, 0]))
    label = "Knight"

    r = Board(np.zeros((8, 8)) + 1.0 / len(k.moves))
    r.rewards[-1][0] = 1.0
    r.rewards[0][-1] = 1.0
    r.rewards[0][0] = 0.0
    r.rewards[-1][-1] = 0.0
    r.rewards[3][3] = 1.0
    r.rewards[4][4] = 1.0
    r.rewards[3][4] = 0.0
    r.rewards[4][3] = 0.0

    inp = np.array(
        [
            r.state(np.array([row, col]))
            for row in range(r.dims[0])
            for col in range(r.dims[1])
        ]
    )

    out = np.array(
        [
            k.rollout(
                r,
                k.moves.values(),
                np.array([row, col]),
                3,
            )
            for row in range(r.dims[0])
            for col in range(r.dims[1])
        ]
    )

    result = []
    files = []
    for epoch in range(100):
        history = k.model.fit(
            inp,
            out,
            epochs=1,
            batch_size=64,
            verbose=0,
        )

        result.append(history.history[[i for i in history.history.keys()][-1]])
        sns.set(rc={"figure.figsize": (15, 6)})
        fig, axs = plt.subplots(ncols=3)
        mainColor = 0x8FCACA
        colorWeight = 0x0A0A0A
        sns.lineplot(
            data=np.array(result),
            color={0: f"#{hex(mainColor)[2:].zfill(6)}"},
            ax=axs[0],
        )
        sns.lineplot(
            data=k.model.predict(inp),
            palette={
                0: f"#{hex(mainColor - colorWeight*8)[2:].zfill(6)}",
                1: f"#{hex(mainColor - colorWeight*7)[2:].zfill(6)}",
                2: f"#{hex(mainColor - colorWeight*6)[2:].zfill(6)}",
                3: f"#{hex(mainColor - colorWeight*5)[2:].zfill(6)}",
                4: f"#{hex(mainColor - colorWeight*4)[2:].zfill(6)}",
                5: f"#{hex(mainColor - colorWeight*3)[2:].zfill(6)}",
                6: f"#{hex(mainColor - colorWeight*2)[2:].zfill(6)}",
                7: f"#{hex(mainColor - colorWeight*1)[2:].zfill(6)}",
                8: f"#{hex(mainColor - colorWeight*0)[2:].zfill(6)}",
            },
            dashes={0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""},
            ax=axs[1],
        )
        heatmap_data = np.array(
            [
                np.mean(i)
                for i in k.model.predict(
                    np.array(
                        [
                            r.state(np.array([row, col]))
                            for col in range(r.dims[1])
                            for row in range(r.dims[0])
                        ]
                    )
                )
            ]
        ).reshape((8, 8))
        sns.heatmap(
            data=heatmap_data,
            ax=axs[2],
            cbar=False,
            cmap=sns.light_palette("#957DAD", as_cmap=True, reverse=True),
        ).invert_yaxis()

        files.append(f"./results/{epoch}.png")
        plt.savefig(files[-1])
        plt.close()

    with imageio.get_writer(f"./{label}.gif", mode="I") as writer:
        for file in files:
            image = imageio.imread(file)
            writer.append_data(image)
        for _ in range(36):
            image = imageio.imread(files[-1])
            writer.append_data(image)

    for file in set(files):
        os.remove(file)
