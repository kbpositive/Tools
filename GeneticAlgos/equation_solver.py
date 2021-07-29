import operator
import random
import math

genome = {
    "0": [0.0, [0.0, 0.0, 0.0, 0.0, 0.0]],
    "1": [1.0, [0.0, 0.0, 0.0, 0.0, 1.0]],
    "2": [2.0, [0.0, 0.0, 0.0, 1.0, 0.0]],
    "3": [3.0, [0.0, 0.0, 0.0, 1.0, 1.0]],
    "4": [4.0, [0.0, 0.0, 1.0, 0.0, 0.0]],
    "5": [5.0, [0.0, 0.0, 1.0, 0.0, 1.0]],
    "6": [6.0, [0.0, 0.0, 1.0, 1.0, 0.0]],
    "7": [7.0, [0.0, 0.0, 1.0, 1.0, 1.0]],
    "8": [8.0, [0.0, 1.0, 0.0, 0.0, 0.0]],
    "9": [9.0, [0.0, 1.0, 0.0, 0.0, 1.0]],
    "+": [operator.add, [0.0, 1.0, 0.0, 1.0, 0.0]],
    "-": [operator.sub, [0.0, 1.0, 0.0, 1.0, 1.0]],
    "*": [operator.mul, [0.0, 1.0, 1.0, 0.0, 0.0]],
    "/": [operator.truediv, [0.0, 1.0, 1.0, 0.0, 1.0]],
}


def orgEval(organism):
    if (
        not type(genome[organism[0]][0]) == type(genome[organism[-1]][0]) == float
        or organism == ""
    ):
        return None
    opers = [0.0, []]
    sign = None
    for index, char in enumerate(organism):
        if type(genome[char][0]) != float:
            if not opers[1]:
                continue
            elif not sign:
                sign = genome[char][0]
                opers[0] = float("".join(opers[1]))
                opers[1] = []
                continue
            elif type(genome[organism[index - 1]][0]) != float:
                return None
            opers[0] = (
                sign(opers[0], float("".join(opers[1])))
                if float("".join(opers[1])) != 0.0
                else 0.0
            )
            opers[1] = []
            sign = genome[char][0]
        else:
            opers[1].append(char)
    if opers[1] and sign:
        opers[0] = (
            sign(opers[0], float("".join(opers[1])))
            if float("".join(opers[1])) != 0.0
            else 0.0
        )
        return opers[0]
    return None


def fitness(organism, target):
    fit = 10.0
    if orgEval(organism) is None:
        fit -= 10.0
    else:
        fit -= math.log(1 + abs(target - orgEval(organism))) / 3
    return fit


def orgSeed(numGenes):
    organism = []
    chromosome = random.choices([0.0, 1.0], k=5 * numGenes)
    for c in range(len(chromosome) // 5):
        for key, (value, gene) in genome.items():
            if gene == chromosome[c * 5 : (c + 1) * 5]:
                organism.append(key)
                continue
    return "".join(organism)


target = 42

print(fitness(orgSeed(7), target))
