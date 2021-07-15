#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    result = []
    d = dict.fromkeys(ranked)
    arr = list(d.keys())
    arr.reverse()
    i = 1
    length = len(arr)

    for c in d:
        d[c] = i
        i += 1
    for c in player:
        if c in d:
            result.append(d[c])
        else:
            pos = length - bisect_right(arr, c)
            if pos != len(arr):
                result.append(pos + 1)
            else:
                result.append(length + 1)
    return result


if __name__ == "__main__":

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print("\n".join(map(str, result)))

