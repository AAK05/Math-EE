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

if __name__ == "__main__":
    writejson(sysrandom(),"sysTRNG.json")
