def nxt(invert, arr, side, pivot):
    return next(
        invert * ind
        for ind, val in enumerate(arr[::invert], invert * side)
        if invert * val >= invert * pivot
    )


def sort(arr: list) -> list:
    stack = [[0, len(arr) - 1]]
    while stack:
        cur = stack.pop()

        if cur[0] < cur[1]:
            left, right, pivot = cur[0], cur[1], arr[(cur[0] + cur[1]) // 2]

            while left <= right:
                left = nxt(1, arr[left:], left, pivot)
                right = nxt(-1, arr[: right + 1], right, pivot)
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1

            index = left
            stack.extend([[index, cur[1]], [cur[0], index - 1]])
    return arr


if __name__ == "__main__":
    import random

    assert sort(random.sample(range(20), k=20)) == list(range(20))
