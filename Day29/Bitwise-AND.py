#!/bin/python3

import math
import os
import random
import re
import sys

#Function to find A&B
def bitwiseAnd(N, K):
    max_val = 0
    for i in range(K-2,N):
        for j in range(i+1,N+1):
            val = i&j
            if val == K-1:
                return val
            if max_val<val<K:
                max_val = val
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')
