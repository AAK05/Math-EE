import json
with open("coprime-digits-2023-1000k.json","r") as f:
    p = json.load(f)
def modulo(data,max=10):
    s = []
    for i in data:
        s.append(i%max)
    return s
n = modulo(p,10)
with open("coprime-digits-mod10-2023-1000k.json","w") as f:
    json.dump(n,f)