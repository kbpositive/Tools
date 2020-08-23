import random
import string


# create random set of lowercase ascii characters

random_string = lambda n : ''.join(random.sample(string.ascii_lowercase, n))

# count nodes in set

count = lambda graph, nodes : [row[0] for row in list(graph.values())].count(nodes)

# find root of graph

def find(graph, node):
  root = graph[node][1]
  while root != graph[root][1]:
    root = graph[root][1]
  return root

# unify two nodes in graph

def union(graph, pair):
  rootA = find(graph, pair[0])
  rootB = find(graph, pair[1])
  if rootA != rootB:
    if count(graph, graph[rootA][0]) <= count(graph, graph[rootB][0]):
      graph[rootB] = graph[rootA]
      graph[pair[1]] = graph[rootA] # path compression
    else:
      graph[rootA] = graph[rootB]
      graph[pair[0]] = graph[rootB] # path compression

# run through node pairings in a graph and return a minimum spanning tree

def union_find(graph, pairings):
  for pair in pairings:
    union(graph, pair)
  return graph

# create random set with enumerated values

nodes = random_string(8)
tree = {}
for i, j in enumerate(nodes):
  tree[j] = [i, j]

# random pairings between nodes

pairings = []
for i in range(2):
  rand_list = random.sample(list(tree), len(tree))
  pairings.extend([[rand_list[i], rand_list[i + (len(tree) //  2)]] for i in range(len(tree) //  2)])

#print('Default Nodes:\n' + '\n'.join(['{} - {}, {}'.format(item[0], item[1][1], item[1][0]) for item in tree.items()]))
#print('Pairings:\n' + '\n'.join(['{} - {}'.format(pair[0], pair[1]) for pair in pairings]))
#print('Minimum Spanning Tree:\n' + '\n'.join(['{} - {}, {}'.format(item[0], item[1][1], item[1][0]) for item in union_find(tree, pairings).items()]))