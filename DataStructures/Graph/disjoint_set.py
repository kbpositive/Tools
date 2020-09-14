import random


def gen(nodes):
    a = [i for i in range(nodes)]
    b = a[:]
    random.shuffle(a)
    random.shuffle(b)
    grph = {}
    for key, pair in enumerate(zip(a, b)):
        grph[key] = pair
    return grph


class DisjointSet:
    def __init__(self, nodes: int):
        self.graph = gen(nodes)
