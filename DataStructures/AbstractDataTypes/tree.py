class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class AVLNode:
	def __init__(self, parent=None, val=0, left=None, right=None):
		self.parent = parent
		self.val = val
		self.left = left
		self.right = right
		self.height = 0
		self.bf = 0
