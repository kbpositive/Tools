from DataStructures.Tree.Nodes import regular
class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.func = lambda x: print(x.val)

    def insert(self, item):
        if self.root is None:
            self.root = Node(item)
            return
        current = self.root
        while current.val != item:
            if current.val < item:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(item)
                    return
            elif current.val > item:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(item)
                    return
        return "Item already exists."

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

    def traverse(self, order='in'):
        if self.root is not None:
            current = self.root
            stack = []
            if order == 'pre':
                self.func(node)
                self.traverse(node.left, order)
            elif order == 'in':
                if current is not None:
                    while current is not None:
                        stack.append(current)
                        current = current.left
                    current = stack.pop()
                    self.func(current)
                    current = current.right
                else:
                    current = stack.pop()
                while stack:
                    if current is not None:
                        while current is not None:
                            stack.append(current)
                            current = current.left
                        current = stack.pop()
                        self.func(current)
                        current = current.right
                    else:
                        current = stack.pop()
            elif order == 'post':
                self.func(node)
            else:
                return "Invalid search order."
        return "Empty Tree."

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

t = Tree()
for i in range(10):
    t.insert(i)
t.traverse()
