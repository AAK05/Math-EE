from encryption1 import generatekey

def freq_analysis(key):
    distribution={}
    for i in key:
        distribution[i] = distribution.get(i,0) + 1
    return distribution

print(freq_analysis(generatekey(100000)))
#Frequency analysis of pi digits
"""
from pi import pi

key = pi(10000)
distribution={}
for i in key:
    distribution[i] = distribution.get(i,0) + 1
print(distribution)
"""