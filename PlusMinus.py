#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#



def plusMinus(arr):
    length = len(arr)
    positives = 0
    zeros = 0
    negatives = 0
    
    # Write your code here
    for x in arr:
        if x > 0:
            #if x is greater then 0 (positive)
            positives += 1
        elif x == 0:
            #if x is equal to 0 
            zeros += 1
        elif x < 0:
            #if x is less then 0 (negative)
            negatives += 1
            
    
    print(positives/length)
    print(negatives/length)
    print(zeros/length)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)