node = lambda x: [x, [None, None]]
tree = node(5)

for num in [2, 8, 0, 4, 6, 10, 1, 3, 7, 9]:
    current = tree
    while current[1][current[0] < num]:
        current = current[1][current[0] < num]
    current[1][current[0] < num] = node(num)

# pre order
print("Pre-Order Traversal")
stack = [tree]
while stack:
    current = stack.pop()
    if current:
        stack.extend([current[1][1], current[1][0]])
        print(current[0])

# in order
print("In-Order Traversal")
stack = [[tree, None]]
while stack:
    current = stack.pop()
    if current[0]:
        stack.extend([[current[0][1][1], current[0][0]], [current[0][1][0], None]])
    if current[1]:
        print(current[1])

# post order
print("Post-Order Traversal")
stack = [[tree, []]]
while stack:
    current = stack.pop()
    if current[0]:
        current[1].append(current[0][0])
        stack.extend([[current[0][1][1], current[1]], [current[0][1][0], []]])
    else:
        while current[1]:
            print(current[1].pop())

# level order
print("Level-Order Traversal")
stack = [tree]
while stack:
    current = stack.pop(0)
    if current:
        print(current[0])
        stack.extend(current[1])

if __name__ == "__main__":
    pass
