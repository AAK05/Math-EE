from encryption1 import generatekey

key = generatekey(100000)
distribution={}
for i in key:
    distribution[i] = distribution.get(i,0) + 1
print(distribution)

#Frequency analysis of pi digits
"""
from pi import pi

key = pi(10000)
distribution={}
for i in key:
    distribution[i] = distribution.get(i,0) + 1
print(distribution)
"""