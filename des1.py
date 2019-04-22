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

PT1 = numpy.arange(0,56)

random.shuffle(PT1)
print("Original array A : ",A)
print()
new_A = Permutation(A,PT1)
print("Permuted array : ",new_A)
print()
right_array,left_array = split_in_two(new_A)
print("Left array : ",left_array)
print("Right array : ",right_array)
print()
left_shift_Left_Arr = circular_left_shift(left_array,1)
left_shift_Right_Arr = circular_left_shift(right_array,2)
print("Left array after circular : ",left_shift_Left_Arr)
print("Right array after circular : ",left_shift_Right_Arr)
