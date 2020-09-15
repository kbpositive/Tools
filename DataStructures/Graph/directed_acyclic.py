import random


def gen(nodes):
    a = [i for i in range(nodes)]
    random.shuffle(a)
    grph = {item: {node: random.randint(0, 9) for node in a[key + 1:min(((key + 1) + random.randint(1, 3)), len(a))]} for key, item in enumerate(a[:-1])}
    grph[a[-1]] = {a[-1]: 0}
    return grph


class Graph:
    def __init__(self, nodes: int):
        self.graph = gen(nodes)
