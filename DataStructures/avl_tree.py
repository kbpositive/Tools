from DataStructures.AbstractDataTypes import tree


class AVLTree:
	def __init__(self):
		self.root = None
		self.size = 0
		self.func = print

	def update(self, node):
		lh = -1
		rh = -1
		if node.left is not None:
			lh = node.left.height
		if node.right is not None:
			rh = node.right.height
		node.height = 1 + max([lh, rh])
		node.bf = rh - lh
		return node

	def rotate(self, child, direction: str):
		if direction == 'right':
			parent = child.left
			child.left = parent.right
			parent.right = child
			self.update(child)
			self.update(parent)
			return parent
		elif direction == 'left':
			parent = child.right
			child.right = parent.left
			parent.left = child
			self.update(child)
			self.update(parent)
			return parent

	def case(self, case_type: str, node):
		if case_type == 'll':
			return self.rotate(node, 'right')
		elif case_type == 'lr':
			node.left = self.rotate(node.left, 'left')
			return self.case('ll', node)
		elif case_type == 'rr':
			return self.rotate(node, 'left')
		elif case_type == 'rl':
			node.right = self.rotate(node.right, 'right')
			return self.case('rr', node)

	def balance(self, node):
		if node.bf == -2:
			if node.left.bf <= 0:
				return self.case('ll', node)
			else:
				return self.case('lr', node)
		elif node.bf == 2:
			if node.right.bf >= 0:
				return self.case('rr', node)
			else:
				return self.case('rl', node)
		return node

	def insert(self, item, node):
		if node is None:
			return tree.AVLNode(None, item, None, None)
		else:
			if item is node.val:
				return node
			elif node.val < item:
				node.right = self.insert(item, node.right)
				self.size += 1
			else:
				node.left = self.insert(item, node.left)
				self.size += 1
		self.update(node)
		return self.balance(node)

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

h = AVLTree()

for i in range(20):
	h.root = h.insert(i%10, h.root)

h.traversal(h.root, 'post')
