import numpy as np

table = [['*', '*', '*'],
         ['*', '*', '*'],
         ['*', '*', '*']]

list = ['*', '*', '*']

def hill_encrypt(key, plaintext):

    i = 0

    for row in range(3):
        for col in range(3):
            table[row][col] = ord(key[i])-65
            i = i+1

    cipher = ""

    for i in range(0,len(plaintext),3):
        list = plaintext[i:i+3]
        list2 = [ord(j)-65 for j in list ]
        #print(list2)
        #for i in range(3):
        #ord(key[i])-65
        #print(,i)
        a = np.array(table)
        b = np.array(list2)
        mat = np.matmul(a, b)
        mat = [i%26 for i in mat]
        mat2 =[chr(i+65) for i in mat]
        text = ''.join(map(str,mat2))
        #print(text)
        cipher = cipher + text

    return cipher

def print_table():
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
