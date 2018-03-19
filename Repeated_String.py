#!/bin/python3

import sys

def repeatedString(s, n):
    my_list = []
    true_remain = []
    division, remain= divmod(n, len(s))
    beloved_str = "a"
    for i in range(len(s)):
        if s[i] == beloved_str:
            my_list.append(1)
   
    number_of_a = sum(my_list)
    external_a = s[0:remain]
    for i in range(len(external_a)):
        if external_a[i] == beloved_str:
            true_remain.append(1)

    total_found = (number_of_a * division) + sum(true_remain)

    return total_found

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
