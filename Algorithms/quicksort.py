def partition(arr: list, pivot: int, left: int, right: int) -> int:
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
    return left


def quicksort(arr: list, left: int, right: int):
    if left < right:
        pivot = arr[(left + right) // 2]
        index = partition(arr, pivot, left, right)
        quicksort(arr, left, index - 1)
        quicksort(arr, index, right)
    return arr


def sort(arr: list) -> list:
    quicksort(arr, 0, len(arr) - 1)
    return arr
