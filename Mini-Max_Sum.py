#!/bin/python3

import sys

def miniMaxSum(arr):
    minimal = min(arr)  
    maximal = max(arr)
    maximum_val = sum(arr) - minimal
    minimal_val = sum(arr) - maximal
    result = print(minimal_val, maximum_val)
    return result

    
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
