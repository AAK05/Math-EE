from list_add import list_add
import json

def loadkeysbase10(keyjsons,length):
    data = []
    output = []
    for keyjson in keyjsons:
        with open(keyjson,"r") as keyfile:
            key = json.load(keyfile)
        data = list_add(data,key,length)
    for i in data:
        n = i%10
        output.append(n)
    return output

def convertbase26(data):
    output = []
    buffer = 0
    print("Creating buffer")
    for i in data:
        buffer *= 10
        buffer += i
    print("Converting buffer to base26")
    while buffer != 0:
        output.append(buffer%26)
        buffer = buffer//26
    output = output[::-1]
    return output

def writejson(obj,fname="testkeygen3.json"):
    with open(fname,"w") as f:
        json.dump(obj,f)

if __name__=="__main__":
    sequences = (
        "coprime-digits-mod10-2023-1000k.json",
        "pi-digits.json",
        #"sqrt-2-1000000dp.json"
    )
    data = loadkeysbase10(sequences,length=1000000)
    data26 = convertbase26(data)
    writejson(data26)