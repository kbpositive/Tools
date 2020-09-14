from Algorithms.Functions import graph as graph_algo


def sort_edges(graph: dict) -> dict:
	return dict(sorted(graph.items(), key=lambda x: x[1]))


def union_find(graph: dict, pairings: list) -> dict:
	graph = sort_edges(graph)
	for pair in pairings:
		graph_algo.union(graph, pair)
	return graph
