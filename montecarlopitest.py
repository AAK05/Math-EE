from sklearn import preprocessing
import numpy as np

def distancetocentre(x,y,centerx=0.5,centery=0.5):
    dist = ((x-centerx)**2 + (y-centery)**2)**0.5
    return dist

def MonteCarloPi(datax,datay=None):
    x = np.array(datax).reshape(-1,1)
    scaler = preprocessing.MinMaxScaler()
    normalizedx = scaler.fit_transform(x)
    normalizedx = normalizedx.reshape(1,-1)
    if datay == None:
        normalizedy=normalizedx
    else:
        y = np.array(datay).reshape(-1,1)
        scaler = preprocessing.MinMaxScaler()
        normalizedy = scaler.fit_transform(y)
        normalizedy = normalizedy.reshape(1,-1)
    normalizedx = normalizedx.tolist()
    normalizedx = normalizedx[0]
    normalizedy = normalizedy.tolist()
    normalizedy = normalizedy[0]
    n=0
    inside = 0
    outside = 0
    for i in normalizedx:
        dist = distancetocentre(i,normalizedy[n])
        n+=1
        if dist <= 0.5:
            inside += 1
        else:
            outside += 1
    pi = 4*(inside/(inside+outside))
    return pi

"""from RNG_div_all_Coprime import DivAllCoPrimeRNG
print(MonteCarloPi(DivAllCoPrimeRNG(2003),DivAllCoPrimeRNG(2011)))"""
"""import quantumrandom
lst1 = []
lst2 = []
for i in range(10):
    lst1.append(quantumrandom.get_data(array_length=1000))
    lst2.append(quantumrandom.get_data(array_length=1000))
    if i%10 == 0:
        print(str(i)+"%")
print(MonteCarloPi(lst1,lst2))"""