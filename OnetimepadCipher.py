#One Time Pad Cipher is a method of encrypting alphabetic text.
#It uses a simple form of polyalphabetic substitution.
# In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked,
#but requires the use of a one-time pre-shared key the same size as, or longer than, the message being sent.

#In this technique, a plaintext is paired with a random secret key (also referred to as a one-time pad). 4
#Then, each bit or character of the plaintext is encrypted by combining it with the corresponding bit or
#character from the pad using modular addition.

#Encryption
#The the plaintext(P) and key(K) are added modulo 26.
#Ei = (Pi + Ki) mod 26

#Decryption
#Di = (Ei - Ki + 26) mod 26
import random     # for generating random

key = []    #The randomly generated key

def OTP_encrypt(plaintext): #Encryption Function sequence
    cipher = ""
    n = len(plaintext)

    plaintext = plaintext.upper()

    create_key(n)
    print(key)

    for i in range(n):
         a = ord(plaintext[i])-65
         b = key[i]
         c = (a + b)%26               #Ei = (Pi + Ki) mod 26
         cipher = cipher + chr(c+65)

    return (cipher)



def create_key(n):       #For generating random sequence of length = len(plaintext)

    global key
    key = [random.randrange(1+i,10+i) for i in range(n) ]
    print(key)



def OTP_decrypt(cipher):       #Decryption Functiom
    n = len(cipher)
    plaintext = ""
    for i in range(n):
         a = ord(cipher[i])-65
         b = key[i]
         c = (a - b)%26           #Di = (Ei - Ki + 26) mod 26
         plaintext = plaintext + chr(c+65)

    return (plaintext)






if __name__ == "__main__":
    p = input("Enter the plaintext key : ") #input the plaintext
    print()
    cipher = OTP_encrypt(p)         #Calling encryption function
    print("Encrypted cipher : ",cipher)
    print()
    print("Decrypted cipher : ",OTP_decrypt(cipher))  #Calling decryption function
