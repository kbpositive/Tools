class Heap:
    def __init__(self, heap_type='max', vals=None):
        if vals is None:
            vals = []
        self.vals = []
        self.type = heap_type
        self.insert(vals)

    def delete(self):
        item = self.vals[0]
        self.vals[0] = self.vals[-1]
        self.vals.pop()
        element = 0

        def direction(children: int) -> bool:
            if self.type == 'max':
                return max([self.vals[2 * element + i] for i in range(1, children + 1)]) > self.vals[element]
            if self.type == 'min':
                return min([self.vals[2 * element + i] for i in range(1, children + 1)]) < self.vals[element]
            raise KeyError('\'type\' must be either \'min\' or \'max\'.')

        def right_child() -> bool:
            if self.type == 'max':
                return self.vals[2 * element + 1] > self.vals[2 * element + 2]
            if self.type == 'min':
                return self.vals[2 * element + 1] < self.vals[2 * element + 2]
            raise KeyError('\'type\' must be either \'min\' or \'max\'.')

        while (2 * element + 1) <= len(self.vals) - 1:
            if (2 * element + 2) <= (len(self.vals) - 1) and direction(2):
                child = 1 if right_child() else 2
            elif direction(1):
                child = 1
            else:
                break

            temp = self.vals[2 * element + child]
            self.vals[2 * element + child] = self.vals[element]
            self.vals[element] = temp
            element = 2 * element + child
        return item

    def insert_element(self, item):
        self.vals.extend([item])
        element = len(self.vals) - 1

        def direction() -> bool:
            if self.type == 'max':
                return self.vals[(element - 1) // 2] < self.vals[element]
            if self.type == 'min':
                return self.vals[(element - 1) // 2] > self.vals[element]
            raise KeyError('\'type\' must be either \'min\' or \'max\'.')

        while element and direction():
            temp = self.vals[element]
            self.vals[element] = self.vals[(element - 1) // 2]
            self.vals[(element - 1) // 2] = temp
            element = (element - 1) // 2

    def insert(self, elements: list):
        for element in elements:
            self.insert_element(element)
