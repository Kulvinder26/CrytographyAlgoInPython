import random
import numpy
from numpy import *
import math

def Permutation(Arr,Permutation_table):
    New_A = []
    for i in Permutation_table:
        New_A.append(A[i])

    return(New_A)

def create_s_box():
    s_box = numpy.random.randint(16,size = (4,16)).tolist()
    return s_box

def convert2binary(n):
    binary = []
    for i in range(4):
        k = n%2
        binary.append(int(k))
        n = floor(n/2)
    binary = numpy.flip(binary).tolist()

    return (binary)


def s_box_permutation(A):
    Arr = []
    for i in range(0,len(A),6):
        #Arr = A[i:i+6]
        Arr.append(A[i:i+6].tolist())
    #print(Arr)
    s_box = []
    Encrypted = []
    for i in range(0,8):
        s_box.append(create_s_box())
    for i in range(0,8):
        K = Arr[i][:2] + Arr[i][4:]
        K = numpy.flip(K)
        K2 = Arr[i][2:4]
        K2 = numpy.flip(K2)
        p = 0
        p2 = 0
        #print(K2)
        for t in range(0,4):
            p = p + K[t]*(2**t)
        for t in range(0,2):
            p2 = p2 + K2[t]*(2**t)
        #s_box[i][p]
        #print("K iz",K,i,p,p2)
        #print("s_box_value : ",s_box[i][p2][p])

        Encrypted.append(convert2binary(s_box[i][p2][p]))
        #print(s_box[i])
        #print()
        #print()
    Final_array = []
    for i in range(8):
        Final_array = Final_array + Encrypted[i]

    return(Final_array)




A = numpy.random.randint(2,size = 48)


print("Original array A : ",A,len(A))
print()

A = s_box_permutation(A)

#convert2binary(13)

PT1 = numpy.arange(0,32)

random.shuffle(PT1)
#print("Ye dekho",PT1)
new_A = Permutation(A,PT1)
print("Permuted array : ",new_A,len(new_A))
print()
