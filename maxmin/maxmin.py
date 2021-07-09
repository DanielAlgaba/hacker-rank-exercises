import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    unfairness = math.inf
    s = sorted(arr)

    i = 0
    while i + k <= len(s):
        diff = s[i + k - 1] - s[i]
        if diff < unfairness:
            unfairness = diff
        i += 1
    return unfairness


if __name__ == "__main__":
    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    print(maxMin(k, arr))
