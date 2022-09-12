import random
import json

def writejson(obj,fname):
    with open(fname,"w") as f:
        json.dump(obj,f)

def sysrandom(len=1000000):
    #Using random module
    #Making the rng use systemrandom, which is TRNG, not PRNG
    rng = random.SystemRandom()
    sys = []
    for i in range(len):
        sys.append(rng.randint(1,26))
    return sys

def randorg():
    output = []
    with open("2022-08-01.txt","r") as file:
        bitsource = file.readline()
    decimal = int(bitsource,2)
    print("Converting randorgTRNG to base26")
    #Convert to base26
    while decimal != 0:
        output.append(decimal%26)
        decimal = decimal//26
    output = output[::-1]
    return output

if __name__ == "__main__":
    writejson(sysrandom(),"sysTRNG.json")
    writejson(randorg(),"randorgTRNG.json")
