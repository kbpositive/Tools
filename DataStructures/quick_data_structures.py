import random

def link(data): return [data, None]

def node(data): return [data, {0:None, 1:None}]

def letter(data): return [data,[None]*128]

def vertices(n): return {num:index for index,num in enumerate(random.sample(range(n),k=n))}

def edges(v,n): return [random.sample(v.keys(),k=2) for _ in range(n)]

def linked_list(n):
    head = link(-1)
    current = head
    nxt = 1

    for next_num in random.sample(range(n),k=n):
        current[nxt] = link(next_num)
        current = current[nxt]
    return head

def tree(n):
    root = node(-1)
    val = 0
    nxt = 1

    for next_num in random.sample(range(n),k=n):
        current = root
        while current[nxt][current[val] < next_num]:
            current = current[nxt][current[val] < next_num]
        current[nxt][current[val] < next_num] = node(next_num)
    return root

def trie(words):
    root = letter("")
    nxt = 1

    for word in words:
        current = root
        for char in word:
            if current[nxt][ord(char)] is None:
                current[nxt][ord(char)] = letter(char)
            current = current[nxt][ord(char)]
    return root

def adj_list(v,e,directed=False):
    verts = vertices(v)
    edgs = edges(verts,e)
    adj_list = {}

    frm = 0
    to = 1

    for pair in edgs:
        for vertex in pair:
            if vertex not in adj_list:
                adj_list[vertex] = {}
        adj_list[pair[frm]][pair[to]] = adj_list[pair[to]]
        if not directed:
            adj_list[pair[to]][pair[frm]] = adj_list[pair[frm]]
    return adj_list

def adj_mat(v,e,directed=False,weighted=False):
    verts = vertices(v)
    edge_sets = zip(edges(verts,e), random.sample(range(e),k=e))
    edgs = [[edge_set[0][0],edge_set[0][1],edge_set[1]] for edge_set in edge_sets]
    adj_mat = [[0]*v for row in range(v)]
    frm = 0
    to = 1

    for triplet in edgs:
        for vertex in triplet[:2]:
            if vertex not in verts:
                verts[vertex] = len(adj_mat)
                adj_mat.append([0]*len(adj_mat))
                for row in adj_mat:
                    row.append(0)
        adj_mat[verts[triplet[frm]]][verts[triplet[to]]] = 1*(triplet[2]**int(weighted))
        if adj_mat[verts[triplet[to]]][verts[triplet[frm]]] == 0:
            adj_mat[verts[triplet[to]]][verts[triplet[frm]]] = (-1*(triplet[2]**int(weighted)))**int(directed)
    return adj_mat

if __name__ == '__main__':
    # linked list
    print(linked_list(7),end='\n\n')

    # tree
    print(tree(25))

    # trie
    print(trie(["lions","tigers","bears"]))

    # graph: adjacency list
    print(adj_list(9,10,directed=True))

    # graph: adjacency matrix
    print(adj_mat(5,10,weighted=True,directed=True))

    print("\npass")
