#!/bin/python3

import sys
a = "#" 
def staircase(n):
    
    for i in range(n):
        result = print((a*(i+1)).rjust(n)) 
    return result

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
