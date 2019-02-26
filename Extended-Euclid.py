
#In arithmetic and computer programming,
#the extended Euclidean algorithm is an extension to the Euclidean algorithm,
#and computes, in addition to the greatest common divisor of integers a and b,
#also the coefficients of Bézout's identity, which are integers x and y such that,
#      ax + by = gcd(a,b)


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
    print()
    print(str(a)+"*"+str(c)+ " + "  + str(b) +"*"+str(d) +" = " +"gcd(" + str(_)+ ")")        #ax + by = gcd(a,b)
