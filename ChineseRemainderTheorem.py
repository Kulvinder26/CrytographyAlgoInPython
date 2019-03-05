# Chinese Remainder Theorem:   If m1, m2, .., mk are pairwise relativelyprime positive integers,
# and if a1, a2, .., ak are any integers, then the simultaneous congruences

# x≡a1 (mod m1),    x≡a2 (mod m2),   ...,   x≡ak (mod mk), have a solution,
#and the solution is unique modulo m, where m = m1 m2⋅⋅⋅mk.



import numpy as np  # for faster manipulation of arrays
import math

item = [1,1]
arr = []
m = []
y = []



def MultiplicativeInv(x,y):   # to calculate multiplicative Inverse
    if y == 0:
        return (x,1,0);
    else :
        d,a,b = MultiplicativeInv(y,x%y)

        return (d,b,a-(math.floor(x/y)*b))



def chineseRT(q):   # to find the x using Chinese Remainder Theorem

    k = 1
    N = np.array(arr)
    M = N[:,0]
    N = N[:,1]

    Num = np.prod(N)

    for i in range(q):
        m[i] = int(Num/N[i])

    for i in range(q):

        _,c,d = MultiplicativeInv(m[i],N[i])
        if c < 0:
            c = N[i]+c
        y[i] = c

    p = 0
    for i in range(q):
        l = (M[i]*m[i]*y[i])
        p = p + l

    p = p%Num
    return p



if __name__ == "__main__":
    d = int(input("Enter number of equation of form 'x = a(mod p)' : "))

    for row in range(d):
        rowdata = []
        rowdata.append(1)
        rowdata.append(1)
        arr.append(rowdata)
        m.append(1)
        y.append(1)

    for row in range(d):
        k = input("Enter 'a' and 'p' seperated by ',' : ")
        k = k.split(',')
        for col in range(2):
            arr[row][col]=int(k[col])

    X = chineseRT(d)      # calling the function
    print("The x is : ",X)
