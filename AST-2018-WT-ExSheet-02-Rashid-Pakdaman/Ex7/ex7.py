import numpy as np

def funCalc(inList):
    lst2 = [1-x for x in inList]
    lst3 = [a/b for a,b in zip(inList,lst2)]
    return 1-((1 + np.product(lst3))**(-1))

def valueCalc(k,n):
    valList = [0.5]
    for i in range(k-2):
        valList.append(0.9)
    for i in range((n+1)-k):
        valList.append(0.1)
    return valList

if __name__ == '__main__':
    seriesValue = []
    seriesValue.append( funCalc(valueCalc(10,20)) )
    seriesValue.append( funCalc(valueCalc(100,120)) )
    # seriesValue.append( funCalc(valueCalc(1000,1200)) )
    # seriesValue.append( funCalc(valueCalc(10000,10200)) )
    print(seriesValue)
