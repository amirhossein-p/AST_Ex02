import numpy as np
import random

def genRan(n1, n2, n3):
    ranList = []
    for i in range(n1):
        ranList.append(random.uniform(n2, n3))
    return ranList

def calcSum(inList):
    return np.sum(inList)

def calcProduct(inList):
    return np.prod(inList)

def calcAverage(inList):
    return np.average(inList)

def calcVariance(inList):
    return np.var(inList)

def calcMin(inList):
    return np.min(inList)

def calcMax(inList):
    return np.max(inList)



if __name__ == '__main__':
    rands = []
    while(True):
        n1 = int(input('Enter integer n1 (1 - 1,000,000) : '))
        if (n1 <= 10000000) and (n1 > 0) :
            break
        else:
            print('Please enter integer between 1 & 1,000,000!')
    n2 = int(input('Enter integer n2 (1 - 1,000,000) : '))
    while(True):
        n3 = int(input('Enter integer n3 (n2 < n3) : '))
        if (n3 > n2):
            break
        else:
            print('Please enter integer grater than ',n2, '!')
    rands = genRan(n1, n2, n3)
    print('sum = ',round(calcSum(rands), 3))
    print('product = ', round(calcProduct(rands), 3))
    print('average = ', round(calcAverage(rands), 3))
    print('variance = ', round(calcVariance(rands), 3))
    print('min = ', round(calcMin(rands), 3))
    print('max = ', round(calcMax(rands), 3))
