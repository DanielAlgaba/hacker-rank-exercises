#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def lilysHomework(arr):
    beauty = list(sorted(arr))
    reversed_beauty = list(reversed(beauty))
    count = 0
    second_count = 0
    l1 = arr.copy()
    l2 = arr.copy()
    pos1 = {}
    pos2 = {}

    for i in range(len(arr)):
        pos1.setdefault(arr[i], i)
        pos2.setdefault(arr[i], i)
    for i in range(len(arr)):
        if l1[i] != beauty[i]:
            aux = l1[i]
            idx = pos1[beauty[i]]
            l1[i] = beauty[i]
            l1[idx] = aux
            pos1[beauty[i]] = i
            pos1[aux] = idx
            count += 1
        if l2[i] != reversed_beauty[i]:
            aux = l2[i]
            idx = pos2[reversed_beauty[i]]
            l2[i] = reversed_beauty[i]
            l2[idx] = aux
            pos2[reversed_beauty[i]] = i
            pos2[aux] = idx
            second_count += 1
    return min(count, second_count)


if __name__ == "__main__":

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(lilysHomework(arr))

