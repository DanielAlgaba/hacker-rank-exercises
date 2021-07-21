#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#


def biggerIsGreater(w):
    if w == "".join(sorted(w, reverse=True)):
        return "no answer"
    else:
        idx = 0
        for i in range(len(w) - 2, -1, -1):
            if w[i] < w[i + 1]:
                idx = i
                break
        arr = w[idx + 1 :]
        aux = w[idx]
        origin = idx
        min = w[idx + 1]
        idx += 1
        for j in range(1, len(arr)):
            if arr[j] > aux:
                min = arr[j]
                idx += 1
            else:
                break
        return w[:origin] + min + "".join(sorted(w[origin:idx] + (w[idx + 1 :])))


if __name__ == "__main__":

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        print(biggerIsGreater(w))

