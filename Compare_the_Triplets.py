#!/bin/python

import sys
A = 0
B = 0
def solve(a0, a1, a2, b0, b1, b2):
    global A
    global B
    if (a0 < b0) :
        B = B+1
    elif a0 == b0:
        A = A
        B = B 
    else :
        A = A+1
    if (a1 < b1) :
        B = B+1
    elif a1 == b1:
        A = A
        B = B 
    else :
        A = A+1
    if (a2 < b2) :
        B = B+1
    elif a2 == b2:
        A = A
        B = B 
    else :
        A = A+1        
    result = str(A)+str(B)    
    return result    
    # Complete this function

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
