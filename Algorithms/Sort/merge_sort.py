def sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    halves = [sort(arr[:middle]),sort(arr[middle:])]
    size = sum([len(halves[0]),len(halves[1])])
    return [min([i for i in halves if i]).pop(0) for _ in range(size)]


if __name__ == '__main__':
    assert sort([4,3,5,2,6,7,1]) == [1,2,3,4,5,6,7]
    pass
