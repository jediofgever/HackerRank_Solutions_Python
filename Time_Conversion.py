#!/bin/python3

import sys
am = "AM"
pm = "PM"
 
def timeConversion(s):
    if s[8:10] == am:
        if int(s[0:2]) >= 12:
            new_time = str(0)+str(0)+s[2:8]
        else :    
            new_time = s[0:8]
    if s[8:10] == pm:
        if int(s[0:2]) >= 12:
            new_time = str(12)+s[2:8]
        else:
            
            converted = int(s[0:2])+12
            new_time = str(converted)+s[2:8]
        
    return new_time
s = input().strip()
result = timeConversion(s)
print(result)
