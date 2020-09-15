def count(graph, value) -> int:
	return [row[1] for row in list(graph.values())].count(value)


def find_root(graph, node):
	root = node
	while root not in list(graph[root].keys()):
		root = list(graph[root].keys())[0]
	return root


def union(graph, pair):
	root_a = find_root(graph, pair[0])
	root_b = find_root(graph, pair[1])
	if root_a != root_b:
		if count(graph, graph[root_a][1]) <= count(graph, graph[root_b][1]):
			graph[root_b] = graph[root_a]
			graph[pair[1]] = graph[root_a]  # path compression
		else:
			graph[root_a] = graph[root_b]
			graph[pair[0]] = graph[root_b]  # path compression

from DataStructures.Graph import directed_acyclic

b = directed_acyclic.Graph(10)
print(b.graph)
print(find_root(b.graph, 5))
