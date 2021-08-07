import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import imageio
import os


class board:
    pass


class piece:
    def __init__(self, pos):
        self.pos = pos


class king(piece):
    pass
