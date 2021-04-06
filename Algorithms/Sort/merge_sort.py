def sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    elif len(arr) < 3:
        return [min(arr), max(arr)]
    middle = len(arr) // 2
    temp = []
    left = sort(arr[:middle])
    right = sort(arr[middle:])
    for i in range(len(left) + len(right)):
        if min([len(left), len(right)]) > 0:
            if left[0] < right[0]:
                temp.append(left[0])
                del left[0]
            else:
                temp.append(right[0])
                del right[0]
        else:
            break
    if len(left) < len(right):
        temp.extend(right)
    else:
        temp.extend(left)
    return temp

if __name__ == '__main__':
    assert sort([4,3,5,2,6,7,1]) == [1,2,3,4,5,6,7]
    pass
