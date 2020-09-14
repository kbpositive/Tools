def count(graph, value) -> int:
	return [row[1] for row in list(graph.values())].count(value)


def find(graph, node):
	root = graph[node][0]
	while root != graph[root][0]:
		root = graph[root][0]
	return root


def union(graph, pair):
	root_a = find(graph, pair[0])
	root_b = find(graph, pair[1])
	if root_a != root_b:
		if count(graph, graph[root_a][1]) <= count(graph, graph[root_b][1]):
			graph[root_b] = graph[root_a]
			graph[pair[1]] = graph[root_a]  # path compression
		else:
			graph[root_a] = graph[root_b]
			graph[pair[0]] = graph[root_b]  # path compression
