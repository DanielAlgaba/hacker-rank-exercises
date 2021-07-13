#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

# Complete the triplets function below.
def triplets(a, b, c):
    a.sort()
    c.sort()
    da = list(dict.fromkeys(a).keys())
    db = dict.fromkeys(b)
    dc = list(dict.fromkeys(c).keys())
    count = 0

    for i in db:
        n1 = bisect_right(da, i)
        n2 = bisect_right(dc, i)
        count += n1 * n2
    return count


if __name__ == "__main__":
    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    print(triplets(arra, arrb, arrc))

