from div_digits import divide
from math import gcd
import numpy as np

def DivAllCoPrimeRNG(limit,dp=10000):
    data = []
    v2 = -1
    for i in range(limit):
        if gcd(i+1,limit)==1:
            a = divide(limit,i+1,dp)
            v1 = np.array(a)
            if isinstance(v2,int):
                v2 = v1
            else:
                v2 = np.add(v1,v2)
    data = v2.tolist()
    print(len(data))
    return data

#from autocorrelation import correlogram
#print(correlogram(DivAllCoPrimeRNG(7919,10000),20))
    