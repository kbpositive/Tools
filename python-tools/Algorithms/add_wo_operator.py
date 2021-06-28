def add(x,y):
    bins = [list(f'{x:b}'),list(f'{y:b}')]
    summation = []
    remainder = 0

    while bins:
        if len(bins) > 1:
            sum1,sum2 = int(bins[0].pop()),int(bins[1].pop())
            sum3 = (sum1^sum2)^remainder

            if sum1 == sum2 == 1 or sum1^sum2 == remainder == 1:
                remainder = 1

            summation.append(str(sum3))

            if not bins[1]:
                if remainder:
                    bins[1].append(remainder)
                    remainder = 0
                else:
                    bins.pop()
                    
            if not bins[0]:
                bins.pop(0)

        else:
            for _ in range(len(bins[0])):
                summation.append(str(bins[0].pop()))

            bins.pop()

    output = ''.join([x for y in ['0b',summation[::-1]] for x in y])

    return int(output,2)

if __name__ == '__main__':
    add(42,8)
