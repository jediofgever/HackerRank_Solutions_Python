#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    result = sum(ar)
    return result
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(long, raw_input().rstrip().split())

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
