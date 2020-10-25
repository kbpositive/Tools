from DataStructures.Tree.Nodes import regular


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.func = lambda x: print(x.val)

    def insert_node(self, item, node):
        if node is None:
            return regular.Node(item, None, None)
        else:
            if item is node.val:
                return node
            elif node.val < item:
                node.right = self.insert_node(item, node.right)
                self.size += 1
            else:
                node.left = self.insert_node(item, node.left)
                self.size += 1
        return node

    def insert(self, item):
        self.root = self.insert_node(item, self.root)

    def remove_node(self, item, node=None):
        if node is None:
            return node
        elif node.val > item:
            node.left = self.remove_node(item, node.left)
        elif node.val < item:
            node.right = self.remove_node(item, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                self.size -= 1
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                self.size -= 1
                return temp
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.val = temp.val
            temp = None
            self.size -= 1
        return node

    def remove(self, item):
        self.remove_node(item, self.root)

    def traverse_tree(self, node, order):
        if node is None:
            return None
        if order == 'pre':
            self.func(node)
        self.traverse_tree(node.left, order)
        if order == 'in':
            self.func(node)
        self.traverse_tree(node.right, order)
        if order == 'post':
            self.func(node)

    def traversal(self, order='in'):
        self.traverse_tree(self.root, order)

    def find_node(self, item, node=None):
        if node is None:
            raise ValueError('Item not found.')
        elif node.val != item:
            if item < node.val:
                return self.find_node(item, node.left)
            else:
                return self.find_node(item, node.right)
        else:
            return node

    def find(self, item):
        return self.find_node(item, self.root)
