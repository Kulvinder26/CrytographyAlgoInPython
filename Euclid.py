#In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient method for computing
#the greatest common divisor (GCD) of two numbers, the largest number that divides both of them without leaving a remainder.
#It is named after the ancient Greek mathematician Euclid, who first described it in his Elements (c. 300 BC).


#Euclid's algorithm

def gcd(a,b):
    if b == 0:
        return a;
    else :
        return gcd(b,a%b)





if __name__ == "__main__":
    a = int(input("Enter first number :"))
    b = int(input("Enter second number (mod by no.):"))
    #print(a,b)
    d = gcd(a,b)
    print("Greatest Common Divisor of " + str(a) + " and "+ str(b)+" : ",d)
