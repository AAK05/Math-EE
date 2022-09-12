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
    graph = {}
    for k in range(1,maxk+1):
        graph[k] = autocorrelation(data,k)
    return graph

def max_autocorr(data,maxk=100):
    graph = correlogram(data,maxk)
    kmax = max(graph,key=graph.get)
    p = graph[kmax]
    return (kmax,p)

#To find most negative autocorrelation
def min_autocorr(data,maxk=100):
    graph = correlogram(data,maxk)
    kmin = min(graph,key=graph.get)
    p = graph[kmin]
    return (kmin,p)

def plot_correlogram(data,maxk=100):
    import numpy as np
    import matplotlib.pyplot as plt
    graph = correlogram(data,maxk)
    x = np.linspace(1,maxk,maxk)
    y = np.array([graph[i] for i in range(1,maxk+1)])
    plt.grid()
    plt.plot(x,y,marker=".",color="b")
    plt.xlabel("Lag (k)")
    plt.ylabel("Autocorrelation")
    #plt.legend()
    plt.show()

#data = [23.4,24.1,44.4,25.5,29.2,37.1,45.0,61.8,56.7,62.3,30.9,69.6,11.0,56.6,83.4,33.9,75.5,87.3,55.4,95.2]
#print(autocorrelation(data,2))