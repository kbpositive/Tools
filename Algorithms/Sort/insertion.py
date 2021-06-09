def sort(arr):
    arr_copy = arr[:]

    for indx in range(len(arr_copy) - 1):
        arr_copy[indx : indx + 2] = arr_copy[indx : indx + 2][
            :: (-1) ** ((arr_copy[indx] < arr_copy[indx + 1]) + 1)
        ]

        for prev in range(indx - 1, -1, -1):
            arr_copy[prev : prev + 2] = arr_copy[prev : prev + 2][
                :: (-1) ** ((arr_copy[prev] < arr_copy[prev + 1]) + 1)
            ]

    return arr_copy


def sort_in_place(arr):
    for indx in range(len(arr) - 1):
        if arr[indx] > arr[indx + 1]:
            arr[indx : indx + 2] = arr[indx : indx + 2][::-1]

        for prev in range(indx - 1, -1, -1):
            if arr[prev] > arr[prev + 1]:
                arr[prev : prev + 2] = arr[prev : prev + 2][::-1]

    return arr


if __name__ == "__main__":
    import random

    arr = random.sample(range(10), k=10)

    assert sort(arr) == list(range(10))

    assert sort_in_place(arr) == list(range(10))
