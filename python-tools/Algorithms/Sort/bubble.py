def sort(arr):
    for _ in range(len(arr)):
        for indx in range(len(arr) - 1):
            if arr[indx] > arr[indx + 1]:
                arr[indx : indx + 2] = arr[indx : indx + 2][::-1]
    return arr


if __name__ == "__main__":
    import random

    assert sort(random.sample(range(10), k=10)) == list(range(10))
