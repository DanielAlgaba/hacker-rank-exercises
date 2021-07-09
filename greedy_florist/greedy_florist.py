import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    costs = {}
    number_flowers = {}
    aux = sorted(c, reverse=True)

    for j in range(k):
        costs.setdefault(j, 0)
        number_flowers.setdefault(j, 1)
        costs[j] += aux[j]

    for x in aux[j + 1 :]:
        aux = min(costs, key=costs.get)
        costs[aux] += (number_flowers[aux] + 1) * x
        number_flowers[aux] += 1
    return sum(costs.values())


if __name__ == "__main__":
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    print(getMinimumCost(k, c))
