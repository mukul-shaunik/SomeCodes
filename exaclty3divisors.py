''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Complete this function
from math import sqrt,floor
def isPrime(N):
    if(N == 1 or N==4):
        return False
    elif N==2 or N==3:
        return True
    flag = True
    for i in range(2,N):
        if N%i == 0:
            flag = False
            break
    return flag

def exactly3Divisors(N):
    c = 0
    for i in range(1,N+1):
        sq = sqrt(i)
        if floor(sq).real == sq and isPrime(floor(sq)):
            c += 1
    return c
        
    ##Your code here
