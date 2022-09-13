import csv
from autocorrelation import *
from dig_transition import *
from freq_analysis import *
from montecarlopitest import *
from difftests import *
import json

def createcsv(distribution,name):
    with open(name,"w",newline="") as f:
        writer = csv.writer(f)
        for key in sorted(distribution.keys()):
            writer.writerow((key,distribution[key]))

if __name__ == "__main__":
    with open("Amber-Spyglass_Encrypted-Enumerated.json","r") as f:
        cipher = json.load(f)

    with open("randorgTRNG3.json","r") as f:
        trng = json.load(f)
    trng = trng[0:len(cipher)]

    createcsv(freq_analysis(cipher),"freq-analysis-cipher.csv")
    createcsv(freq_analysis(trng),"freq-analysis-trng.csv")
    createcsv(difftest(cipher),"difftest-cipher.csv")
    createcsv(difftest(trng),"difftest-trng.csv")
    createcsv(slopetest(cipher),"slopetest-cipher.csv")
    createcsv(slopetest(trng),"slopetest-trng.csv")
    createcsv(correlogram(cipher),"correlogram-cipher.csv")
    createcsv(correlogram(trng),"correlogram-trng.csv")