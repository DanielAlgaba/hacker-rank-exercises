#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    s = str(s)
    count = 0
    l = [s[x:y] for x, y in combinations(range(len(s) + 1), r=2)]
    d = dict.fromkeys(l)
    for c in d:
        d[c] = l.count(c)
    aux = {}

    for c in d:
        sort = "".join(sorted(c))
        aux.setdefault(sort, 0)
        aux[sort] += d[c]
    for x in aux:
        count += (aux[x] * (aux[x] - 1)) / 2
    return int(count)


if __name__ == "__main__":
    fptr = open(os.getenv("OUTPUT_PATH", "."), "w")

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + "\n")

    fptr.close()
