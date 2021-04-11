class Node:
    def __init__(self, parent=None, val=0, left=None, right=None):
        self.parent = parent
        self.val = val
        self.left = left
        self.right = right
        self.height = 0
        self.bf = 0


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def update(self, node):
        lh = node.left.height if node.left else -1
        rh = node.right.height if node.right else -1
        node.height = 1 + max([lh, rh])
        print(node.height)
        node.bf = rh - lh

    def rotate(self, child, direction):
        if direction == "right":
            parent = child.left
            child.left = parent.right
            parent.right = child
        elif direction == "left":
            parent = child.right
            child.right = parent.left
            parent.left = child
        self.update(child)
        self.update(parent)
        return parent

    def case(self, case_type: str, node):
        if case_type == "ll":
            return self.rotate(node, "right")
        elif case_type == "lr":
            node.left = self.rotate(node.left, "left")
            return self.case("ll", node)
        elif case_type == "rr":
            return self.rotate(node, "left")
        elif case_type == "rl":
            node.right = self.rotate(node.right, "right")
            return self.case("rr", node)

    def balance(self, node):
        if node.bf < -1:
            return self.case("ll" if node.left.bf <= 0 else "lr", node)
        elif node.bf > 1:
            return self.case("rr" if node.right.bf >= 0 else "rl", node)
        return node

    def insert(self, item):
        if self.root:
            current = self.root
            while [current.left, current.right][current.val < item]:
                current = [current.left, current.right][current.val < item]
            setattr(current, ["left", "right"][current.val < item], Node(current, item))
            current = [current.left, current.right][current.val < item]
        else:
            self.root = Node(val=item)
            current = self.root

        self.size += 1
        self.update(current)
        return self.balance(current)

    def remove(self, item):
        current = self.find(item)
        case = bool(current.left) + bool(current.right)
        replacement = None

        if case > 1:
            successor = current.right
            while successor.left or successor.right:
                successor = successor.left if successor.left else successor.right
            current.val = successor.val

            current = successor
        elif case > 0:
            replacement = current.left if current.left else current.right

        setattr(
            current.parent, ["left", "right"][current.parent.val < item], replacement
        )

        self.size -= 1
        self.update(current)
        return self.balance(current)

    def print_tree_pre(self):
        output = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current:
                stack.extend([current.right, current.left])
                # print([current.height, current.bf])
                output.append(current.val)
        return output

    def find(self, item):
        if self.root:
            current = self.root
            while [current.left, current.right][
                current.val < item
            ] and current.val != item:
                current = [current.left, current.right][current.val < item]

            if current.val == item:
                return current

        raise ValueError("Item not found.")


if __name__ == "__main__":
    T = Tree()
    vals = [5, 2, 4, 3, 0, 1, 8, 6, 7, 10, 9]
    for val in vals:
        T.insert(val)

    assert T.print_tree_pre() == [5, 2, 0, 1, 4, 3, 8, 6, 7, 10, 9]
    assert T.find(4).val == 4
    assert T.find(5).val == 5

    T.remove(4)
    T.remove(8)
    T.remove(7)

    assert T.print_tree_pre() == [5, 2, 0, 1, 3, 9, 6, 10]

    G = Tree()
    for val in range(25):
        G.insert(val)
    print(G.print_tree_pre())
    print("pass")