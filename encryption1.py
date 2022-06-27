from fibonacci import fibonacci
from pi import pi

def generatekey(keylength):
    fibonacci_lst = fibonacci(keylength)
    pi_lst = pi(keylength)
    key = []
    for i in range(0,keylength):
        element = (fibonacci_lst[i]+pi_lst[i])%26
        key.append(element)
    return key

def encrypt(message):
    message = message.replace(" ","") #Cleaning input
    message = message.lower() #Cleaning input
    message_lst_chars = [] #list of characters in message
    message_lst = [] #List of message as numerals where a=1, b=2, etc
    encrypted_lst_char = [] #List of characters of ciphertext
    encrypted_lst = [] #List of ciphertext as numerals
    for letter in message: #converts plaintext str to lst
        message_lst_chars.append(letter)
    for char in message_lst_chars: #converts plaintext lst of chars to numbers
        message_lst.append(ord(char)-96)
    #print(message_lst)
    key_lst = generatekey(len(message_lst))
    #print(key_lst)
    for n in range(0,len(message_lst)): #Modulo arithmetic to encrypt plaintext
        element = (message_lst[n] + key_lst[n])%26
        encrypted_lst.append(element)
    #print(encrypted_lst)
    for x in encrypted_lst:
        if x==0: #0 as 26, because modulo 26 returns 0
            encrypted_lst_char.append("z")
        else: #Converts ciphertext lst of numbers to chars
            encrypted_lst_char.append(chr(x+96))
    encrypted = "".join(encrypted_lst_char)
    return encrypted

if __name__ == "__main__":
    print(encrypt("Secret Message"))