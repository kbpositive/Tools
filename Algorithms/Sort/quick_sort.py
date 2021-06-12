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


def quicksort(arr: list, left: int, right: int) -> list:
    if left < right:
        pivot = arr[(left + right) // 2]
        index = partition(arr, pivot, left, right)
        quicksort(arr, left, index - 1)
        quicksort(arr, index, right)
    return arr


def sort(arr: list) -> list:
    return quicksort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    assert sort([6, 5, 7, 4, 8, 3, 9, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
