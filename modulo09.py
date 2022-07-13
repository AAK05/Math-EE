import json
with open("coprime-digits.json","r") as f:
    p = json.load(f)
def modulo(data,max=10):
    s = []
    for i in data:
        s.append(i%max)
    return s
n = modulo(p,10)
with open("coprime-digits-mod10.json","w") as f:
    json.dump(n,f)