#!/bin/python

import sys

def diagonalDifference(a):
    diag_nor = 0
    diag_rev = 0
    reverse_a = a[::-1] 
    for i in range(n):
        diag_nor += a[i][i]
        diag_rev += reverse_a[i][i]
    result = abs(diag_nor-diag_rev)
    return result

 
                        
if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(a)
    print result
