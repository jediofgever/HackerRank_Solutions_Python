#!/bin/python3

import sys

def jumpingOnClouds(c):
    c.insert(n,0)
    i = 0 
    count = 0 
    while i < n-1:
        i += (c[i+2] == 0) + 1 
        count += 1
    return count    
            

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c)
    print(result)
