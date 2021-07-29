import operator
import random

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


def opEval(op1, oper, op2):
    return genome[oper][0](float(op1), float(op2))


def orgEval(organism):
    opers = [0.0, []]
    sign = None
    for char in organism:
        if type(genome[char][0]) != float:
            if not opers[1]:
                continue
            elif not sign:
                sign = genome[char][0]
                opers[0] = float("".join(opers[1]))
                opers[1] = []
                continue
            opers[0] = sign(opers[0], float("".join(opers[1])))
            opers[1] = []
            sign = genome[char][0]
        else:
            opers[1].append(char)
    if opers[1]:
        opers[0] = sign(opers[0], float("".join(opers[1])))
    return opers[0]


orgEval("/2+32/7-")
