import random
import numpy

A = "Meet me in the Park"

key = numpy.arange(0,25)
random.shuffle(key)
print(key)

plaintext = []
cipher = ""
A = A.upper()
A = A.split(" ")
A = ''.join(map(str,A))
print(A)
keys = []
for i in A:
    index = ord(i)-65
    p = key[index]
    keys.append(p)
    p = (index + p)%26
    print(p)
    p = chr(p+65)
    cipher = cipher + p
print("Plaintext : ",A)
print("Cipher : ",cipher)
print(keys)
Decrypted_text = ""

for i in range(len(cipher)):
    index = ord(cipher[i])-65
    print(p)
    p = (index - keys[i])%26
    p = chr(p+65)
    Decrypted_text = Decrypted_text + p

print(Decrypted_text)
