def merge_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    elif len(arr) < 3:
        return [min(arr), max(arr)]
    middle = len(arr) // 2
    temp =  []
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
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