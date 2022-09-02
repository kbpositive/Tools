from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.orders = {n: True for n in ["level", "pre", "in", "post"]}
        self.size = len(self.print_tree())

    def print_tree(self, order="in"):
        if order not in self.orders:
            raise ValueError("Invalid search order.")

        output = []
        if order == "pre" or order == "level":
            stack = deque([self.root])
        else:
            stack = [[self.root, None]]

        if order == "level":
            while stack:
                current = stack.popleft()
                if current:
                    output.append(current.val)
                    stack.extend(deque([current.left, current.right]))

        elif order == "pre":
            while stack:
                current = stack.pop()
                if current:
                    output.append(current.val)
                    stack.extend([current.right, current.left])

        elif order == "in":
            while stack:
                current = stack.pop()
                if current[1] is not None:
                    output.append(current[1])
                if current[0]:
                    stack.extend(
                        [[current[0].right, current[0].val], [current[0].left, None]]
                    )

        elif order == "post":
            while stack:
                current = stack.pop()
                if current[1] and current[0]:
                    current[1].append(current[0].val)
                    stack.extend(
                        [[current[0].right, current[1]], [current[0].left, None]]
                    )
                else:
                    while current[1]:
                        output.append(current[1].pop())
                    if current[0]:
                        current[1] = [current[0].val]
                        stack.extend(
                            [[current[0].right, current[1]], [current[0].left, None]]
                        )

        return output

    def insert(self, item):
        if self.root:
            current = self.root
            
            while (
                [current.left,current.right][current.val < item]
                and current.val != item
                ):
                current = [current.left, current.right][current.val < item]

            if current.val == item:
                raise Exception("Item already exists.")

            setattr(current, ["left","right"][current.val < item], Node(item))

        else:
            self.root = Node(item)

        self.size += 1

    def remove(self, item):
        # if tree is not empty create previous
        # and current variables, both set to the root
        if self.root:
            previous = self.root
            current = previous

            # while there is a next node and the current value is not item,
            # set previous value to current and current value to next node
            while {0: current.left, 1: current.right}[
                current.val < item
            ] and current.val != item:
                previous = current
                current = {0: current.left, 1: current.right}[current.val < item]

            # if current value is equal to item, current becomes
            # the deletion target with its right child as the default
            # replacement
            if current.val == item:
                replacement = current.right

                # if target has both children
                # set parent value to target
                if current.right and current.left:
                    parent = current

                    # while replacement exists and has a left child
                    # set parent value to replacement value
                    # and replacement value to its left child
                    while replacement and replacement.left:
                        parent = replacement
                        replacement = replacement.left

                    # set left child of replacement's parent
                    # to replacement's right child; set replacement's
                    # left child to the target's left child; set the
                    # replacement's right child to the parent
                    parent.left = replacement.right
                    replacement.left = current.left
                    replacement.right = parent

                # if target only has either a left or right node,
                # this node becomes the replacement
                elif current.right:
                    replacement = current.right
                elif current.left:
                    replacement = current.left

                # if current is the root, set root to the replacement node
                # otherwise set the next node
                # (based on whether previous.val < item) to the replacement node
                if current is self.root:
                    self.root = replacement
                else:
                    setattr(
                        previous,
                        {0: "left", 1: "right"}[previous.val < item],
                        replacement,
                    )

                # increment tree size by 1
                self.size -= 1

        # otherwise, the item is not in the tree
        else:
            raise Exception("Item not in tree.")
