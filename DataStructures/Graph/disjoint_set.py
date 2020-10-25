import random


def gen(nodes):
    a = [i for i in range(nodes)]
    b = a[:]
    random.shuffle(a)
    random.shuffle(b)
    grph = {pair[0]: {pair[1]: random.randint(1, 9)} for pair in zip(a, b)}
    return grph


class Graph:
    def __init__(self, nodes: int):
        self.graph = gen(nodes)
