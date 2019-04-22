import random
import numpy


def split_in_two(Arr):
    L_A = Arr[:28]
    R_A = Arr[28:]
    return(R_A,L_A)

def circular_left_shift(Arr,n_bit):
    left_shift_Arr = Arr[n_bit:] + Arr[:n_bit]
    return(left_shift_Arr)

def Permutation(Arr,Permutation_table):
    New_A = []
    for i in Permutation_table:
        New_A.append(A[i])

    return(New_A)


A = numpy.random.randint(2,size = 64)

PT1 = numpy.arange(0,64)

random.shuffle(PT1)
print("Original array A : ",A)
print()
new_A = Permutation(A,PT1)
print("Permuted array first: ",new_A)
print()
right_array,left_array = split_in_two(new_A)

PT2 = numpy.random.randint(32,size = 48)

new_A2 = Permutation(A,PT2)
print("Permuted array second: ",new_A2)
print(len(new_A2))
