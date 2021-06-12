def partition(arr: list, pivot: int, left: int, right: int) -> int:
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left


def sort(arr: list) -> list:
    stack = [[0, len(arr) - 1]]
    while stack:
        cur = stack.pop()

        if cur[0] < cur[1]:
            pivot = arr[(cur[0] + cur[1]) // 2]
            index = partition(arr, pivot, cur[0], cur[1])
            stack.extend([[index, cur[1]], [cur[0], index - 1]])
    return arr


if __name__ == "__main__":
    assert sort([6, 5, 7, 4, 8, 3, 9, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
