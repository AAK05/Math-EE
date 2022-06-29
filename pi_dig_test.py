from pi import pi
from autocorrelation import correlogram
from montecarlopitest import MonteCarloPi
from RNG_div_all_Coprime import DivAllCoPrimeRNG

data = pi(200000)
datax = []
data2 = pi(400000)[200000:]
datax2 = []
for i in range(len(data)):
    if i%2 == 0:
        n = str(data[i]) + str(data[i+1]) #+ str(data[i+2]) + str(data[i+3]) + str(data[i+4])
        datax.append(int(n))
for i in range(len(data2)):
    if i%2 == 0:
        n = str(data2[i]) + str(data2[i+1]) #+ str(data2[i+2]) + str(data2[i+3]) + str(data2[i+4])
        datax2.append(int(n))
#print(data)
print(correlogram(data))
print(datax[:5],datax2[:5])
print(MonteCarloPi(datax,datax2))