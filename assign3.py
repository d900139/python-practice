####################
##  assign3.py
####################

import re

def convert_sum(inputnum):
     pattern = '[A-Z]+'
     string = sorted(re.findall(pattern, inputnum))
     arr = []
     for i in range(len(string)):
         temp = 0
         for j in range (len(string[i])):
             val = ord(string[i][j]) - 64
             temp += val
         arr.append(temp * (i+1))
     return sum(arr)
