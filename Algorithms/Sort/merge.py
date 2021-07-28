from collections import deque


def sort(arr: list) -> list:
    stack = [[[], [0, len(arr) - 1]]]

    while stack:
        current = stack.pop()

        if current[1][1] > current[1][0]:
            current[0].append(current[1])

            mean = sum(current[1]) // 2

            stack.append([current[0], [mean + 1, current[1][1]]])
            stack.append([[], [current[1][0], mean]])
            continue

        while current[0]:
            n = current[0].pop()
            tmp = [deque(arr[n[0] : n[1] + 1]), deque(arr[n[1] + 1 :])]
            arr[n[0] : n[1] + 1] = [max(tmp).popleft() for _ in range(n[1] - n[0] + 1)]

    return arr


if __name__ == "__main__":
    import random

    print(sort(random.sample(range(20), k=20)))
    assert sort(random.sample(range(20), k=20)) == [i for i in range(20)]
