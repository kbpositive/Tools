import random

# create max heap
rando = random.sample(range(200),11)
max_heap = []
for num in rando:
    max_heap.append(num)

    element = len(max_heap) - 1
    while element > 0 and max_heap[(element - 1) // 2] < max_heap[element]:
        temp = max_heap[element]
        max_heap[element] = max_heap[(element - 1) // 2]
        max_heap[(element - 1) // 2] = temp
        element = (element - 1) // 2

print(max_heap)

# add element
for i in range(10):
    max_heap.append(random.randrange(200))

    element = len(max_heap) - 1
    while element > 0 and max_heap[(element - 1) // 2] < max_heap[element]:
        temp = max_heap[element]
        max_heap[element] = max_heap[(element - 1) // 2]
        max_heap[(element - 1) // 2] = temp
        element = (element - 1) // 2

print(max_heap)

# delete element
for i in range(10):
    item = max_heap[0]

    max_heap[0] = max_heap[-1]
    max_heap.pop()
    element = 0
    while (2*element + 2) < len(max_heap) and max([max_heap[2*element + 1], max_heap[2*element + 2]]) > max_heap[element]:
        child = 2 if max_heap[2*element + 2] > max_heap[2*element + 1] else 1
        temp = max_heap[2*element + child]
        max_heap[2*element + child] = max_heap[element]
        max_heap[element] = temp
        element = 2*element + child

print(max_heap)

# create min heap
rando = random.sample(range(200),11)
min_heap = []
for num in rando:
    min_heap.append(num)

    element = len(min_heap) - 1
    while element > 0 and min_heap[(element - 1) // 2] > min_heap[element]:
        temp = min_heap[element]
        min_heap[element] = min_heap[(element - 1) // 2]
        min_heap[(element - 1) // 2] = temp
        element = (element - 1) // 2

print(min_heap)

# add element
for i in range(10):
    min_heap.append(random.randrange(200))

    element = len(min_heap) - 1
    while element > 0 and min_heap[(element - 1) // 2] > min_heap[element]:
        temp = min_heap[element]
        min_heap[element] = min_heap[(element - 1) // 2]
        min_heap[(element - 1) // 2] = temp
        element = (element - 1) // 2

print(min_heap)

# delete element
for i in range(10):
    item = min_heap[0]

    min_heap[0] = min_heap[-1]
    min_heap.pop()
    element = 0
    while (2*element + 2) < len(min_heap) and min([min_heap[2*element + 1], min_heap[2*element + 2]]) < min_heap[element]:
        child = 2 if min_heap[2*element + 2] < min_heap[2*element + 1] else 1
        temp = min_heap[2*element + child]
        min_heap[2*element + child] = min_heap[element]
        min_heap[element] = temp
        element = 2*element + child

print(min_heap)