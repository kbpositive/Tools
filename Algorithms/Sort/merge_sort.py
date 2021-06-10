import heapq


def sort(arr: list) -> list:
    stack = [[[], [0, len(arr) - 1]]]
    while stack:
        current = stack.pop()
        if current[1][1] > current[1][0]:
            current[0].append(current[1])
            mean = (current[1][0] + current[1][1]) // 2
            stack.extend(
                [
                    [
                        current[0],
                        [
                            mean + 1,
                            current[1][1],
                        ],
                    ],
                    [
                        [],
                        [
                            current[1][0],
                            mean,
                        ],
                    ],
                ]
            )
        else:
            while current[0]:
                n = current[0].pop()
                tmp = arr[n[0] : n[1] + 1]
                heapq.heapify(tmp)
                arr[n[0] : n[1] + 1] = [heapq.heappop(tmp) for _ in range(len(tmp))]
    return arr


if __name__ == "__main__":
    import random

    z = random.sample(range(20), k=20)
    print(z)
    print(sort(z))

    assert sort(random.sample(range(8), k=8)) == [0, 1, 2, 3, 4, 5, 6, 7]
