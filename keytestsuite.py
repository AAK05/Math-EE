from autocorrelation import *
from dig_transition import *
from freq_analysis import *
from montecarlopitest import *
import sys
import json

fname = sys.argv[1]
#print(fname)
with open(fname,"r") as f:
    data = json.load(f)
    print(len(data))

data1 = data#[0:500000]
data2 = data1[::-1]

#datax and datax2 adds together 1st and 2nd, 3rd and 4th, etc
#E.g: [1,2,3,4,5,6] becomes [12,34,56]
datax1 = []
datax2 = []
for i in range(len(data1)):
    if i%5 == 0:
        n = str(data[i]) + str(data[i+1]) + str(data[i+2]) + str(data[i+3]) + str(data[i+4])
        datax1.append(int(n))
for i in range(len(data2)):
    if i%5 == 0:
        n = str(data2[i]) + str(data2[i+1]) + str(data2[i+2]) + str(data2[i+3]) + str(data2[i+4])
        datax2.append(int(n))

print("Maximum autocorrelation (k,autocorrelation): " + str(max_autocorr(data1,20)))
print("Minimum autocorrelation (k,autocorrelation): " + str(min_autocorr(data1,20)))
print("Maximum pattern error from expected (pattern,%): " + str(max_pattern(data1)))
print("Minimum pattern error from expected (pattern,%): " + str(min_pattern(data1)))
print("Maximum frequency error (digit,%): " + str(max_freq_err(data1)))
print("Minimum frequency error (digit,%): " + str(min_freq_err(data1)))
print("Simulated value of pi: " + str(MonteCarloPi(datax1,datax2)))