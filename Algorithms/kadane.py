def kadane_sum(nums):
    current, best = 0, 0
    for num in nums:
        current, best = max(0,current+num), max(current,best)
    return best

if __name__ == '__main__':
    import random

    test1 = random.choices(range(-50,50),k=50)

    print(kadane_sum(test1))
