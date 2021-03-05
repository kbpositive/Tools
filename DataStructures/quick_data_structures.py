import random

# linked list
link = lambda x: [x,None]
linked_list = link(-1)
current = linked_list
for n in random.sample(range(7),k=7):
    current[1] = link(n)
    current = current[1]
linked_list

# tree
node = lambda x: [x,{0:None, 1:None}]
tree = node(-1)
for n in random.sample(range(25),k=25):
    current = tree
    while current[1][current[0] < n]:
        current = current[1][current[0] < n]
    current[1][current[0] < n] = node(n)
tree

# trie
letter = lambda x: [x,[None]*128]
trie = letter("")
for word in ["lions","tigers","bears"]:
    current = trie
    for char in word:
        if current[1][ord(char)] is None:
            current[1][ord(char)] = letter(char)
        current = current[1][ord(char)]
trie

# graph:adjacency list
dim = 16
vertices = random.sample(range(dim),k=dim)
edges = [random.sample(vertices,k=2) for _ in range(25)]
adj_list = {}
for pair in edges:
    for vertex in pair:
        if vertex not in adj_list:
            adj_list[vertex] = {}
    adj_list[pair[0]][pair[1]] = adj_list[pair[1]]
adj_list

# graph:adjacency matrix
dim = 15
vertices = {num:index for index,num in enumerate(random.sample(range(dim),k=dim))}
edges = [random.sample(vertices.keys(),k=2) for _ in range(25)]
adj_mat = [[0]*dim for i in range(dim)]
for pair in edges:
    for vertex in pair:
        if vertex not in vertices:
            vertices[vertex] = len(adj_mat)
            adj_mat.append([0]*len(adj_mat))
            for row in adj_mat:
                row.append(0)
    adj_mat[vertices[pair[0]]][vertices[pair[1]]] = 1
    adj_mat[vertices[pair[1]]][vertices[pair[0]]] = -1
adj_mat
