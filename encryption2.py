#!/usr/bin/env python3
from list_add import list_add
import json
import string
def loadkeysbase10(*keyjsons,length):
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

def writejson(obj,fname="test.json"):
    with open(fname,"w") as f:
        json.dump(obj,f)

def loadkey(filename):
    with open(filename,"r") as f:
        key = json.load(f)
    return key

def FormatTextToNum(message):
    message = message.replace(" ","") #Cleaning input
    message = message.translate(str.maketrans("","",string.punctuation))
    message = message.lower() #Cleaning input
    message_lst_chars = [] #list of characters in message
    message_lst = [] #List of message as numerals where a=1, b=2, etc
    for letter in message: #converts plaintext str to lst
        message_lst_chars.append(letter)
    for char in message_lst_chars: #converts plaintext lst of chars to numbers
        message_lst.append(ord(char)-96)
    return message_lst

def FormatNumToText(numlst):
    charlst = []
    for num in numlst:
        if num == 0:
            charlst.append("z")
        else:
            charlst.append(chr(num+96))
    chars = "".join(charlst)
    return chars

def encrypt(plaintext,keyfile):
    cipherlst = []
    plainlst = FormatTextToNum(plaintext)
    key = loadkey(keyfile)
    unmodcipherlst = list_add(plainlst,key,length=len(plainlst))
    for i in unmodcipherlst:
        cipherlst.append(i%26)
    ciphertext = FormatNumToText(cipherlst)
    return ciphertext

def decrypt(ciphertext,keyfile):
    plainlst = []
    cipher = FormatTextToNum(ciphertext)
    key = loadkey(keyfile)
    dekey = [-1*x for x in key]
    unmodplainlst = list_add(cipher,dekey,length=len(cipher))
    for i in unmodplainlst:
        plainlst.append(i%26)
    plaintext = FormatNumToText(plainlst)
    return plaintext
x = encrypt("Attack at dawn!!! They are coming","pi-with-coprime2023-b26.json")
print(x)
y = decrypt(x,"pi-with-coprime2023-b26.json")
print(y)

#b26 = convertbase26(loadkeysbase10("coprime-digits-mod10-2023-1000k.json","pi-digits.json",length=1000000))
#b26 = convertbase26(loadkeysbase10("pi-digits.json",length=1000000))
#writejson(b26,"test26v2.json")
#print(convertbase26([3,1,4,1,5,9,2,6,5,3]))