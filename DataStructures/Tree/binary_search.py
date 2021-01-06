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
                while True:
                    if current:
                        self.func(current)
                        stack.append(current)
                        current = current.left
                    else:
                        if stack:
                            current = stack.pop()
                            current = current.right
                        else:
                            break
            elif order == 'in':
                while True:
                    if current:
                        stack.append(current)
                        current = current.left
                    else:
                        if stack:
                            current = stack.pop()
                            self.func(current)
                            current = current.right
                        else:
                            break
            elif order == 'post':
                while True:
                    while current:
                        stack.append(current)
                        # pre order
                        # self.func(current)
                        current = current.left
                        if current is None:
                            # in order
                            # self.func(current)
                            current = stack[-1].right
                    while current == stack[-1].right:
                        current = stack.pop()
                        # post order
                        self.func(current)
                        if stack:
                            if current != stack[-1].right:
                                # in order
                                # self.func(current)
                                current = stack[-1].right
                                break
                        else:
                            break
                    if not stack:
                        break
            else:
                return "Invalid search order."
        else:
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
t.insert(5)
t.insert(2)
t.insert(4)
t.insert(3)
t.insert(0)
t.insert(1)
t.insert(8)
t.insert(6)
t.insert(7)
t.insert(10)
t.insert(9)
t.traverse('pre')

t.traverse('in')
t.traverse('post')
