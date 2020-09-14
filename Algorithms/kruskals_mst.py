from DataStructures.Graph.Functions import union_find


def sort_edges(graph: dict) -> dict:
	return dict(sorted(graph.items(), key=lambda x: x[1]))


def combine(graph: dict, pairings: list) -> dict:
	graph = sort_edges(graph)
	for pair in pairings:
		union_find.union(graph, pair)
	return graph
