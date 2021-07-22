#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def almostSorted(arr):
    s = list(sorted(arr))
    if arr == s:
        print("yes")
    else:
        idx = 0
        for i in range(len(arr)):
            if arr[i] != s[i]:
                idx = i
                break
        j = s.index(arr[idx])
        t = arr.copy()
        t[idx] = s[idx]
        t[j] = s[j]
        if t == s:
            print("yes")
            print(f"swap {idx + 1} {j + 1}")
        else:
            t = []
            t.extend(arr[:idx])
            t.extend(reversed(arr[idx : j + 1]))
            t.extend(arr[j + 1 :])
            if t == s:
                print("yes")
                print(f"reverse {idx + 1} {j + 1}")
            else:
                print("no")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
