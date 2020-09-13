from DataStructures.AbstractDataTypes import tree


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.func = print

    def insert(self, item, node):
        if node is None:
            return tree.Node(item, None, None)
        else:
            if item is node.val:
                return node
            elif node.val < item:
                node.right = self.insert(item, node.right)
                self.size += 1
            else:
                node.left = self.insert(item, node.left)
                self.size += 1
        return node

    def remove(self, item, node):
        if node is None:
            return node
        elif node.val > item:
            node.left = self.remove(item, node.left)
        elif node.val < item:
            node.right = self.remove(item, node.right)
        else:
            if node.left is None:
                temp = node.right
                del node
                self.size -= 1
                return temp
            if node.right is None:
                temp = node.left
                del node
                self.size -= 1
                return temp
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.val = temp.val
            del temp
            self.size -= 1
        return node

    def traversal(self, node=None, order='in'):
        if node is None:
            return None
        if order == 'pre':
            self.func(node.val)
        self.traversal(node.left, order)
        if order == 'in':
            self.func(node.val)
        self.traversal(node.right, order)
        if order == 'post':
            self.func(node.val)

    def find(self, item, node=None):
        if node is None:
            return 'Item not found.'
        elif node.val != item:
            if item < node.val:
                return self.find(item, node.left)
            else:
                return self.find(item, node.right)
        else:
            return node
