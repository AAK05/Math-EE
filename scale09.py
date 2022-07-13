import json
with open("coprime-digits.json","r") as f:
    p = json.load(f)
def minmaxscale(data,minimum,maximum):
    datamin = min(data)
    datamax = max(data)
    normdata = []
    for i in data:
        x1 = minimum + (((i-datamin)*(maximum-minimum))/(datamax-datamin))
        normdata.append(round(x1))
    return normdata
n = minmaxscale(p,0,9)
with open("coprime-digits-norm.json","w") as f:
    json.dump(n,f)