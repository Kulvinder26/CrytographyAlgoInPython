#Vigenere Cipher is a method of encrypting alphabetic text.
#It uses a simple form of polyalphabetic substitution.
#A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets .

#Encryption
#The the plaintext(P) and key(K) are added modulo 26.
#Ei = (Pi + Ki) mod 26

#Decryption
#Di = (Ei - Ki + 26) mod 26

def vigenere_encrypt(key, plaintext): #Encryption Function
    cipher = ""
    n = len(plaintext)

    plaintext = plaintext.upper()
    key = key.upper()
    key = create_key(key,n)

    for i in range(n):
         a = ord(plaintext[i])-65
         b = ord(key[i])-65
         c = (a + b)%26               #Ei = (Pi + Ki) mod 26
         cipher = cipher + chr(c+65)

    return (cipher)


def create_key(key,n): #Decryption Functiom
    key2 = ""
    l = len(key)
    for i in range(n):
        key2 = key2 + key[i%l]
    return key2

def vigenere_decrypt(key, cipher):
    n = len(cipher)
    key = key.upper()
    key = create_key(key,n)
    plaintext = ""
    for i in range(n):
         a = ord(cipher[i])-65
         b = ord(key[i])-65
         c = (a - b)%26           #Di = (Ei - Ki + 26) mod 26
         plaintext = plaintext + chr(c+65)

    return (plaintext)






if __name__ == "__main__":
    s = input("Enter the secret key : ")  #input the key
    p = input("Enter the plaintext key : ") #input the plaintext
    print()
    cipher = vigenere_encrypt(s, p)         #Calling encryption function
    print("Encrypted cipher : ",cipher)
    print()
    print("Decrypted cipher : ",vigenere_decrypt(s, cipher))  #Calling decryption function
