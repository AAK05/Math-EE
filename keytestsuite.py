from autocorrelation import *
from dig_transition import *
from freq_analysis import *
from montecarlopitest import *
from difftests import *
import sys
import json

fname = sys.argv[1]
#print(fname)
with open(fname,"r") as f:
    try:
        data = json.load(f)
    except:
        data = [x for x in str(f.readline())]
    print(len(data))

data1 = data[0:664044]
data2 = data1[::-1]

#datax and datax2 adds together 1st and 2nd, 3rd and 4th, etc
#E.g: [1,2,3,4,5,6] becomes [12,34,56]
datax1 = []
datax2 = []

if max(data1) < 10:
#Combine multiple base 10
    for i in range(5*(len(data1)//5)):
        if i%5 == 0:
            n = str(data[i]) + str(data[i+1]) + str(data[i+2]) + str(data[i+3]) + str(data[i+4])
            datax1.append(int(n))
    for i in range(5*(len(data2)//5)):
        if i%5 == 0:
            n = str(data2[i]) + str(data2[i+1]) + str(data2[i+2]) + str(data2[i+3]) + str(data2[i+4])
            datax2.append(int(n))
else:
#Combine 2 base26 then convert base10
    for i in range(3*(len(data1)//3)):
        if i%3 == 0:
            n = 26*26*data[i] + 26*data[i+1] + data[i+2] #+ data[i+3] + data[i+4]
            datax1.append(int(n))
    for i in range(3*(len(data2)//3)):
        if i%3 == 0:
            n = 26*26*(data2[i]) + 26*(data2[i+1]) + (data2[i+2]) #+ (data2[i+3]) + (data2[i+4])
            datax2.append(int(n))
print(len(datax1),len(datax2))

#Add 2
"""for i in range((2 * len(data1)//2)-2):
    if i%2 == 0:
        n = 0
        for m in range(i,i+2):
            n += data1[m]
        datax1.append(int(n))
for i in range((2 * len(data2)//2)-2):
    if i%2 == 0:
        n = 0
        for m in range(i,i+2):
            n += data2[m]
        datax2.append(int(n))"""

#Add 3
"""for i in range(3*(len(data1)//3)):
    if i%3 == 0:
        n = data[i] + data[i+1] + data[i+2] #+ data[i+3] + data[i+4]
        datax1.append(int(n))
for i in range(3*(len(data2)//3)):
    if i%3 == 0:
        n = (data2[i]) + (data2[i+1]) + (data2[i+2]) #+ (data2[i+3]) + (data2[i+4])
        datax2.append(int(n))"""

print("Maximum autocorrelation (k,autocorrelation): " + str(max_autocorr(data1,20)))
print("Minimum autocorrelation (k,autocorrelation): " + str(min_autocorr(data1,20)))
#plot_correlogram(data1,100)
#print("Maximum pattern error from expected (pattern,%): " + str(max_pattern(data1)))
#print("Minimum pattern error from expected (pattern,%): " + str(min_pattern(data1)))
print("Max diff error (diff,%): " + str(max_diff_error(data1)))
print("Min diff error (diff,%): " + str(min_diff_error(data1)))
print("Max slope error(slope,%): " + str(max_slope_error(data1)))
print("Min slope error(slope,%): " + str(min_slope_error(data1)))
print("Maximum frequency error (digit,%): " + str(max_freq_err(data1)))
print("Minimum frequency error (digit,%): " + str(min_freq_err(data1)))
print("Simulated value of pi: " + str(MonteCarloPi(datax1,datax2)))
#print("Simulated value of pi: " + str(MonteCarloPi(data1,data2)))