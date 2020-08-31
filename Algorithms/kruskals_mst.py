from DataStructures import disjoint_set


def sort(graph: dict) -> dict:
	return dict(sorted(graph.items(), key=lambda x: x[1]))


def union_find(graph, pairings: list) -> disjoint_set.DisjointSet:
	graph = disjoint_set.DisjointSet(sort(graph))
	for pair in pairings:
		graph.union(pair)
	return graph
