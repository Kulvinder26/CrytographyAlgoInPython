# RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission.
# In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret (private).
# In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem".


import math
import random

a,n,b,k,e = 0,0,0,2,3

def isPrime(n,k):                # To check if a given number iv prime or not
    r = 0
    if n <= 1:
        return "composite"
    elif n == 2 or n == 3:
        return "probably prime"
    elif n%2 == 0:
        return "composite"
    else:
        a = n-1
        while(a%2 == 0):
            a = a/2
            r += 1
        d = int((n-1)/(2**r))

        arr = []
        for i in range(0,k):
            u = primalityRabinMiller(n,d)
            arr.append(u)
        print(arr)

        faith = 0
        for i in arr:
            faith = faith + i
        if faith/k >= 0.5:             # Voting and averaging to find what most of tests agree on i.e. prime or composite
            return "probably prime"
        else: return "composite"

seed = 42
random.seed(seed)                      # setting the seed to generate random numbers






def primalityRabinMiller(n,d):         # Miller Rabin Primality test

    a = random.randrange(2,n-2)

    x = (a**d) % n                     # Compute: x = pow(a, d) % n
    if x==1 or x == n-1:
        return 1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return 0
        if (x == n - 1):
            return 1

    return 0

seed = 51
random.seed(seed)                      # setting the seed to generate random numbers


def generate_prime():                 # randomly generating prime numbers
    a1 = 0
    a2 = 0

    while(not(isPrime(a1,5) == "probably prime" and isPrime(a2,5) == "probably prime")):

        a1 = random.randrange(100,200)
        a2 = random.randrange(100,200)

    return (a1,a2)







def create_public_key():        # creating public key (n,e)
    global a
    global b
    a,b = generate_prime()
    prod = a * b
    e = 3

    return prod,e

def create_private_key():        # creating private key (d)
    global k
    global e
    v = (a-1)*(b-1)
    d = ((k*v)+1)/e

    return int(d)

def Encrypt(p):            # Encrypting with public key

    global n
    global e

    n,e = create_public_key()
    cipher = []
    for i in p:
        g = ord(i)-65
        r = (g**e) % n
        cipher.append(r)
    return cipher

def Decrypt(b):             # Decrypting with private key

    d = create_private_key()
    plaintext = []
    for i in b:
        k = (i**d) % n
        g = chr(k+65)
        plaintext.append(g)
    plaintext = ''.join(map(str,plaintext))
    return plaintext


if __name__ == "__main__":
    p = input("Enter the plaintext : ")
    p = p.upper()
    p = [ i for i in p if not i.isspace()]
    p = ''.join(map(str,p))
    print(p)

    cipher = Encrypt(p)
    plaintext = Decrypt(cipher)
    print("Original", p)
    print("Cipher",cipher)
    print("Plaintext",plaintext)
