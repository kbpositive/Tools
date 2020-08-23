def delete(type, heap: list):
    item = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    element = 0
    if type == 'max':
        direction = lambda x : max([heap[2 * element + i] for i in range(1, x+1)]) > heap[element]
        right_child = lambda: heap[2 * element + 1] > heap[2 * element + 2]
    elif type == 'min':
        direction = lambda x : min([heap[2 * element + i] for i in range(1, x+1)]) < heap[element]
        right_child = lambda: heap[2 * element + 1] < heap[2 * element + 2]
    else:
        raise KeyError('\'type\' must be either \'min\' or \'max\'.')

    while (2 * element + 1) <= len(heap) - 1:
        if (2 * element + 2) <= (len(heap) - 1) and direction(2):
            child = 1 if right_child() else 2
        elif direction(1):
            child = 1
        else:
            break

        temp = heap[2 * element + child]
        heap[2 * element + child] = heap[element]
        heap[element] = temp
        element = 2 * element + child
    return item


def insert(type, item, heap: list) -> object:
    heap.extend([item])
    element = len(heap) - 1
    if type == 'max':
        direction = lambda: heap[(element - 1) // 2] < heap[element]
    elif type == 'min':
        direction = lambda: heap[(element - 1) // 2] > heap[element]
    else:
        raise KeyError('\'type\' must be either \'min\' or \'max\'.')

    while element > 0 and direction():
        temp = heap[element]
        heap[element] = heap[(element - 1) // 2]
        heap[(element - 1) // 2] = temp
        element = (element - 1) // 2

