import random


def gen(nodes):
	a = [i for i in range(nodes)]
	b = [i for i in range(nodes)]
	c = [i for i in range(nodes)]
	random.shuffle(a)
	random.shuffle(b)
	random.shuffle(c)
	grph = {}
	for key, pair in enumerate(zip(a, b)):
		grph[key] = pair
	return grph


class DirectedGraph:
	def __init__(self, nodes: int):
		self.graph = gen(nodes)
