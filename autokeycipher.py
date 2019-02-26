#Vigenere Cipher is a method of encrypting alphabetic text.
#It uses a simple form of polyalphabetic substitution.
# It was invented by Blaise de Vigenère in 1586, and is in general more secure than the Vigenere cipher.
#The 'key' for the Autokey cipher is a key word created by concatenating key with plaintext.
#then the indvidual element are taken from both key and plaintext, modulo by 26 and added, hence creating the cipher

#Encryption
#The the plaintext(P) and key(K) are added modulo 26.
#Ei = (Pi + Ki) mod 26

#Decryption
#Di = (Ei - Ki + 26) mod 26

def autokey_encrypt(key, plaintext): #Encryption Function
    cipher = ""
    n = len(plaintext)

    plaintext = plaintext.upper()
    key = key.upper()
    key = create_key(key,plaintext)

    for i in range(n):
         a = ord(plaintext[i])-65
         b = ord(key[i])-65
         c = (a + b)%26               #Ei = (Pi + Ki) mod 26
         cipher = cipher + chr(c+65)

    return (cipher)


def create_key(key,plaintext): #Decryption Functiom
    key2 = key + plaintext
    return key2

def autokey_decrypt(key, cipher,plaintext):
    n = len(cipher)
    key = key.upper()
    key = create_key(key,plaintext)
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
    cipher = autokey_encrypt(s, p)         #Calling encryption function
    print("Encrypted cipher : ",cipher)
    print()
    print("Decrypted cipher : ",autokey_decrypt(s, cipher,p))  #Calling decryption function
