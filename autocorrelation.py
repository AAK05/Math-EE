#!/usr/bin/env python3
def autocovariance(data,k=1):
    n = len(data)
    mean = sum(data)/len(data)
    acv1 = 0
    for i in range(n-k):
        acv1 += (data[i]-mean)*(data[i+k]-mean)
    acv = acv1/n
    return acv

def autocorrelation(data,k=1):
    acf = autocovariance(data,k)/autocovariance(data,0)
    return acf

def correlogram(data,maxk=100):
    correlogram = {}
    for k in range(maxk+1):
        correlogram[k] = autocorrelation(data,k)
    return correlogram


#data = [23.4,24.1,44.4,25.5,29.2,37.1,45.0,61.8,56.7,62.3,30.9,69.6,11.0,56.6,83.4,33.9,75.5,87.3,55.4,95.2]
#print(autocorrelation(data,2))