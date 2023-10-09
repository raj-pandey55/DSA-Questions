#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    n = len(s)
    print(n)
    sqrt = math.sqrt(n)
    
    trunc = math.trunc(sqrt)
    row = 0
    col= 0
    if(trunc*trunc==n):
        row=trunc
        col=trunc
    elif trunc*(trunc+1)<n:
        trunc+=1
        row = trunc
        col = trunc
    else:
        row = trunc
        col = trunc+1
    
    
    
    ans = []
    k=0
    for i in range(row):
        temp =''
        for j in range(col):
            if k>=n:
                temp+=' '
                k+=1
                continue
            temp+=s[k]
            k+=1
        ans.append(temp)
    print(ans)
    res =''
    row = len(ans)
    col = len(ans[0])
    j=0
    while(j!=col):
        i=0
        while(i!=row):
            if(ans[i][j]==' '):
                i+=1
                continue
            res+=ans[i][j]
            i+=1
        res+=' '
        print(res)
        j+=1
        
    
            
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
