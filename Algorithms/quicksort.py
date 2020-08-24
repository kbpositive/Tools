def partition(array: list, pivot: int, left: int, right: int) -> int:
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
    return left

def quicksort(array: list, left: int, right: int) -> list:
    if left >= right:
        return array
    pivot = array[(left + right) // 2]
    index = partition(array, pivot, left, right)
    quicksort(array, left, index - 1)
    quicksort(array, index, right)

def sort(array: list) -> list:
    quicksort(array, 0, len(array) - 1)
    return array
