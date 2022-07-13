import math
def entropy(data):
    datadict = {}
    length = len(data)
    h = 0
    for i in data:
        datadict[i] = datadict.get(i,0) + 1
    #print(datadict)
    charspace = len(datadict.keys())
    #print(charspace)
    for i in datadict.values():
        p = i/length
        #print(p)
        h += p * math.log2(p)
    return -1*h/charspace