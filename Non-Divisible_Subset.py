#!/bin/python

import sys

import collections

def nonDivisibleSubset(k, arr):
    # Complete this function
    cnt = collections.Counter(v%k for v in arr)
    return sum(map(lambda kv: 2 if kv[0] * 2 % k == 0 else (max(kv[1], cnt[k-kv[0]]) if (k-kv[0]) in cnt else kv[1]*2), (kv for kv in cnt.items()))) // 2

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = map(int, raw_input().strip().split(' '))
    result = nonDivisibleSubset(k, arr)
    print result
