class FenwickTree:
    def __init__(self, vals=None):
        if vals is None:
            vals = []
        self.vals = vals
        length = len(self.vals)
        if length > 1:
            for element in range(1, length):
                sub_root = element + (element & -1)
                if sub_root < length:
                    self.vals[sub_root] += self.vals[element]

    def prefix_sum(self, index: int) -> int:
        total = 0
        while index:
            total += self.vals[index]
            index -= (index & -index)
        return total

    def range_query(self, start: int, end: int) -> int:
        return self.prefix_sum(end) - self.prefix_sum(start - 1)

    def point_update(self, pos, val):
        while pos < len(self.vals):
            self.vals[pos] += val
            pos += pos & -pos
