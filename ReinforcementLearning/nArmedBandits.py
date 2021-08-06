import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython import display


class bandit:
    def __init__(self, arms):
        self.arms = arms
        self.actions = np.random.uniform(-1.0, 1.0, arms)
        self.state = np.ones(arms)

    def pull(self):
        return np.array(
            [
                (-1.0) ** int(action > np.random.uniform(-1.0, 1.0))
                for action in self.actions
            ]
        )
