import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    l = sorted(cost)
    for i in range(len(cost)):
        aux = money - cost[i]
        if binary_search(l, aux, 0, len(cost) - 1):
            if aux != cost[i]:
                j = cost.index(aux)
                print(f"{i + 1} {j + 1}")
                break
            elif cost.count(aux) > 1:
                cost.pop(i)
                j = cost.index(aux)
                print(f"{i + 1} {j + 2}")
                break


def binary_search(arr, elem, left, right):
    k = (left + right) // 2

    if left > right:
        return False
    if arr[k] == elem:
        return True
    elif elem < arr[k]:
        return binary_search(arr, elem, left, k - 1)
    else:
        return binary_search(arr, elem, k + 1, right)


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
