#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#


def absolutePermutation(n, k):
    d = {}
    result = []

    for c in range(1, n + 1):
        d.setdefault(c, 1)
    for i in range(1, n + 1):
        aux = i - k
        if aux in d and d[aux] == 1:
            d[aux] = 0
            result.append(str(aux))
        else:
            aux = i + k
            if aux in d and d[aux] == 1:
                d[aux] = 0
                result.append(str(aux))
            else:
                return -1
    return " ".join(result)


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        print(absolutePermutation(n, k))

