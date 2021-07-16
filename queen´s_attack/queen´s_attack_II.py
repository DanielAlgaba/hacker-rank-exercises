#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    d = dict.fromkeys(obstacles)

    for i in range(r_q + 1, n + 1):
        if (i, c_q) not in d:
            count += 1
        else:
            break
    for i in range(r_q - 1, 0, -1):
        if (i, c_q) not in d:
            count += 1
        else:
            break
    for i in range(c_q + 1, n + 1):
        if (r_q, i) not in d:
            count += 1
        else:
            break
    for i in range(c_q - 1, 0, -1):
        if (r_q, i) not in d:
            count += 1
        else:
            break
    for i in range(1, n):
        if (r_q + i, c_q + i) not in d and r_q + i < n + 1 and c_q + i < n + 1:
            count += 1
        else:
            break
    for i in range(1, n):
        if (r_q - i, c_q + i) not in d and r_q - i > 0 and c_q + i < n + 1:
            count += 1
        else:
            break
    for i in range(1, n):
        if (r_q + i, c_q - i) not in d and r_q + i < n + 1 and c_q - i > 0:
            count += 1
        else:
            break
    for i in range(1, n):
        if (r_q - i, c_q - i) not in d and r_q - i > 0 and c_q - i > 0:
            count += 1
        else:
            break
    return count


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(tuple(map(int, input().rstrip().split())))

    print(queensAttack(n, k, r_q, c_q, obstacles))

