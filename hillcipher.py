#Hill cipher is a polygraphic substitution cipher based on linear algebra.
#To encrypt a message, each block of n letters (considered as an n-component vector)
#is multiplied by an invertible n × n matrix, against modulus 26.

#To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption.

import numpy as np

table = [['*', '*', '*'],            #Empty table for storing encryption matrix values
         ['*', '*', '*'],
         ['*', '*', '*']]

list = ['*', '*', '*']

def hill_encrypt(key, plaintext): #Encryption Funciton

    i = 0

    for row in range(3):
        for col in range(3):
            table[row][col] = ord(key[i])-65
            i = i+1

    cipher = ""

    for i in range(0,len(plaintext),3):
        list = plaintext[i:i+3]
        list2 = [ord(j)-65 for j in list ]

        a = np.array(table)
        b = np.array(list2)
        mat = np.matmul(a, b)
        mat = [i%26 for i in mat]
        mat2 =[chr(i+65) for i in mat]
        text = ''.join(map(str,mat2))
        #print(text)
        cipher = cipher + text

    return cipher

def print_table():               #Function to view table elements
    for row in range(3):
        for col in range(3):
            print(table[row][col],end="")
        print("")

if __name__ == "__main__":
    s = input("Enter the 9 character secret key : ")
    p = input("Enter the plaintext : ")
    print()
    print("Encrypted cipher : ",hill_encrypt(s, p))
    print()
    print_table()
