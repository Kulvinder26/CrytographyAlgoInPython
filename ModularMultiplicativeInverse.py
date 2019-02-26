import math

#Extended-Euclid's algorithm

def EE(x,y):
    if y == 0:
        return (x,1,0);
    else :
        d,a,b = EE(y,x%y)

        return (d,b,a-(math.floor(x/y)*b))





if __name__ == "__main__":
    a = int(input("Enter first number :"))
    b = int(input("Enter second number (mod by no.):"))
    #print(a,b)
    _,c,d = EE(a,b)
    print("Multiplicative Inverse of " + str(a) + " : ",c)
