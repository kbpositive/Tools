def partition(arr: list, pivot: int, left: int, right: int) -> int:
    nxt = lambda i, a, h, c: next(
        i * ind for ind, val in enumerate(a, h) if c * val >= c * pivot
    )
    while left <= right:
        left = nxt(1, arr[left:], left, 1)
        right = nxt(-1, arr[: right + 1][::-1], -right, -1)
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
    import random

    assert sort(random.sample(range(20), k=20)) == list(range(20))
