from encryption1 import generatekey

def freq_analysis(key):
    distribution={}
    for i in key:
        distribution[i] = distribution.get(i,0) + 1
    return distribution

def max_freq_err(data):
    distribution = freq_analysis(data)
    maximum = max(distribution,key=distribution.get)
    expected = len(data)/len(distribution)
    error = 100*(distribution[maximum] - expected)/expected
    return (maximum,error)

def min_freq_err(data):
    distribution = freq_analysis(data)
    minimum = min(distribution,key=distribution.get)
    expected = len(data)/len(distribution)
    error = 100*(distribution[minimum] - expected)/expected
    return (minimum,error)
#print(freq_analysis(generatekey(100000)))
#Frequency analysis of pi digits
"""
from pi import pi

key = pi(10000)
distribution={}
for i in key:
    distribution[i] = distribution.get(i,0) + 1
print(distribution)
"""