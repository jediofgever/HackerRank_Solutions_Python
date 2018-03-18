#!/bin/python3

import sys
 
def plusMinus(arr):
    counter_positive = 0
    counter_negative = 0
    counter_zero = 0

    for i in range(n):
        if arr[i]<0:
            counter_negative += 1
        elif arr[i]>0:
            counter_positive += 1
        else :
            counter_zero += 1
        one = format(counter_positive/n, '.6f')
        two = format(counter_negative/n, '.6f')
        three =format(counter_zero/n, '.6f')
        
    result = print(one),"\n",print(two),"\n",print(three),"\n"    
    return  result

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
