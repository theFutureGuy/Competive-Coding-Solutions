import math
import os
import random
import re
import sys


def solve(a,n):
    nb = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            m = max(a[i:j + 1])
            if a[i] * a[j] <= m:
                nb += 1
    return nb

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr,arr_count)

    fptr.write(str(result) + '\n')

    fptr.close()
