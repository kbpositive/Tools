import random


def link(data):
    return [data, None]


def node(data):
    return [data, [None, None]]


def letter(data):
    return [data, [None] * 128]


def vertices(n):
    return set(random.sample(range(n), k=n))


def edges(v, n, acyclic=True):
    return [
        random.sample(list(v), k=2) if acyclic else random.choices(list(v), k=2)
        for _ in range(n)
    ]


def linked_list(n):
    head = link(-1)
    current = head
    nxt = 1

    for next_num in random.sample(range(n), k=n):
        current[nxt] = link(next_num)
        current = current[nxt]
    return head


def tree(n):
    root = node(-1)

    for next_num in random.sample(range(n), k=n):
        current = root
        while current[1][current[0] < next_num]:
            current = current[1][current[0] < next_num]
        current[1][current[0] < next_num] = node(next_num)
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


def adj_list(v, e, directed=False, acyclic=True):
    verts = {vertex: set() for vertex in vertices(v)}
    edgs = edges(verts, e, acyclic)

    frm = 0
    to = 1

    for pair in edgs:
        for vertex in pair:
            if vertex not in verts:
                verts[vertex] = set()

        verts[pair[frm]].add(pair[to])
        if not directed:
            verts[pair[to]].add(pair[frm])

    return verts


def adj_mat(v, e, directed=False, weighted=False, acyclic=True):
    verts = list(vertices(v))
    edge_sets = zip(edges(verts, e, acyclic), random.sample(range(e), k=e))
    edgs = [[edge_set[0][0], edge_set[0][1], edge_set[1]] for edge_set in edge_sets]
    mat = [[0] * v for row in range(v)]

    frm = 0
    to = 1

    for triplet in edgs:
        for vertex in triplet[:2]:
            if vertex not in verts:
                verts[vertex] = len(mat)
                mat.append([0] * len(mat))
                for row in mat:
                    row.append(0)

        mat[verts[triplet[frm]]][verts[triplet[to]]] = 1 * (triplet[2] ** int(weighted))
        if mat[verts[triplet[to]]][verts[triplet[frm]]] == 0:
            mat[verts[triplet[to]]][verts[triplet[frm]]] = (
                -1 * (triplet[2] ** int(weighted))
            ) ** int(directed)
    return mat


if __name__ == "__main__":
    # linked list
    print(linked_list(7), end="\n\n")

    # tree
    print(tree(5))

    # trie
    print(trie(["lions", "tigers", "bears"]))

    # graph: adjacency list
    print(adj_list(9, 10, directed=True, acyclic=False))

    # graph: adjacency matrix
    print(adj_mat(10, 20, weighted=True, directed=True, acyclic=False))

    print("\npass")
