#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    aux = max(arr)[0]
    result = []
    i = 0
    half = len(arr) // 2

    for i in range(int(aux) + 1):
        result.append([])
    for c in arr:
        if i < half:
            result[int(c[0])].append("-")
        else:
            result[int(c[0])].append(c[1])
        i += 1
    for c in result:
        if c:
            print(" ".join(c), end=" ")


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

