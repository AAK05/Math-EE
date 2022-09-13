from autocorrelation import *
from dig_transition import *
from freq_analysis import *
from montecarlopitest import *
from difftests import *
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

with open("Amber-Spyglass_Encrypted-Enumerated.json","r") as f:
    cipher = json.load(f)

with open("randorgTRNG3.json","r") as f:
    trng = json.load(f)
trng = trng[0:len(cipher)]

def plotcorr(data,maxk=100):
    plot_correlogram(data,maxk=maxk)

def plotcorrdouble(data1,data2,maxk=100):
    #import numpy as np
    #import matplotlib.pyplot as plt
    graph1 = correlogram(data1,maxk)
    graph2 = correlogram(data2,maxk)
    x1 = np.linspace(1,maxk,maxk)
    y1 = np.array([graph1[i] for i in range(1,maxk+1)])
    x2 = np.linspace(1,maxk,maxk)
    y2 = np.array([graph2[i] for i in range(1,maxk+1)])
    plt.grid()
    plt.plot(x1,y1,marker=".",color="b",label="Ciphertext Correlogram")
    plt.plot(x2,y2,marker=".",color="r",label="TRNG Correlogram")
    plt.xlabel("Lag (k)")
    plt.ylabel("Autocorrelation")
    plt.legend()
    plt.show()

def plotfreq(data):
    x = np.array(data)
    plt.hist(x,bins=[0.5+i for i in range(27)],color="b",edgecolor="black",linewidth="1.2",density=True)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.ylabel("% Frequency")
    plt.xlabel("Character")
    plt.show()

def plotcarlo(data):
    data1 = data
    data2 = data1[::-1]
    datax1 = []
    datax2 = []
    for i in range(3*(len(data1)//3)):
        if i%3 == 0:
            n = 26*26*data[i] + 26*data[i+1] + data[i+2] #+ data[i+3] + data[i+4]
            datax1.append(int(n))
    for i in range(3*(len(data2)//3)):
        if i%3 == 0:
            n = 26*26*(data2[i]) + 26*(data2[i+1]) + (data2[i+2]) #+ (data2[i+3]) + (data2[i+4])
            datax2.append(int(n))
    x,y = normalizedcarlo(datax1,datax2)
    figure,axes = plt.subplots()
    plt.scatter(x,y,s=0.15,color="b",linewidths=0)
    plt.xlim(0,1)
    plt.ylim(0,1)
    c = plt.Circle((0.5,0.5),0.5,fill=False,edgecolor="black",linewidth=0.5,visible=True)
    axes.add_artist(c)
    plt.show()
    print(MonteCarloPi(x,y))

def plotnextdig(data):
    expected = len(data)/26
    dist = difftest(data)
    x = np.linspace(0,25,26)
    y = np.array([(100*(dist[i]-expected)/expected) for i in range(26)])
    plt.grid()
    plt.plot(x,y,color="r",marker=".")
    plt.xlabel("Difference")
    plt.ylabel("% Error")
    plt.show()

def plotnextdighist(data):
    dist = difftest(data)
    plt.bar(dist.keys(), dist.values(), 1, color='r',edgecolor="black",linewidth=1.2)
    plt.show()

def plotnextdigdouble(data1,data2):
    expected = len(data1)/26
    dist1 = difftest(data1)
    dist2 = difftest(data2)
    x1 = np.linspace(0,25,26)
    x2 = x1
    y1 = np.array([(100*(dist1[i]-expected)/expected) for i in range(26)])
    y2 = np.array([(100*(dist2[i]-expected)/expected) for i in range(26)])
    plt.grid()
    plt.plot(x1,y1,color="b",marker=".",label = "Next Digit Test Ciphertext")
    plt.plot(x2,y2,marker=".",color="r",label="Next Digit Test TRNG")
    plt.xlabel("Difference")
    plt.ylabel("% Error")
    plt.legend()
    plt.show()

def plotslope(data):
    expected = len(data)/26
    dist = slopetest(data)
    x = np.linspace(0,25,26)
    y = np.array([(100*(dist[i]-expected)/expected) for i in range(26)])
    plt.grid()
    plt.plot(x,y,color="r",marker=".")
    plt.xlabel("Difference")
    plt.ylabel("% Error")
    plt.show()

def plotslopedouble(data1,data2):
    expected = len(data1)/26
    dist1 = slopetest(data1)
    dist2 = slopetest(data2)
    x1 = np.linspace(0,25,26)
    x2 = x1
    y1 = np.array([(100*(dist1[i]-expected)/expected) for i in range(26)])
    y2 = np.array([(100*(dist2[i]-expected)/expected) for i in range(26)])
    plt.grid()
    plt.plot(x1,y1,color="b",marker=".",label = "Linearity Test Ciphertext")
    plt.plot(x2,y2,marker=".",color="r",label="Linearity Test TRNG")
    plt.xlabel("Difference")
    plt.ylabel("% Error")
    plt.legend()
    plt.show()

def plotslopehist(data):
    dist = slopetest(data)
    plt.bar(dist.keys(), dist.values(), 1, color='r',edgecolor="black",linewidth=1.2)
    plt.show()

if __name__ == "__main__":
    #plotcorr(cipher)
    #plotcorrdouble(cipher,trng)
    #plotfreq(cipher)
    #plotcarlo(cipher)
    #plotnextdigdouble(cipher,trng)
    #plotnextdighist(trng)
    #plotslope(trng)
    #plotslopedouble(cipher,trng)
    plotslopehist(trng)