import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    costs = {}
    aux = sorted(c, reverse=True)

    for x in range(len(aux)):
        costs.setdefault(x % k, 0)
        costs[x % k] += (x // k + 1) * aux[x]
    return sum(costs.values())


if __name__ == "__main__":
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    print(getMinimumCost(k, c))
