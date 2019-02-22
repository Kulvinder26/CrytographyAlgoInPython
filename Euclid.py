a  = 36
b  = 24
#Euclid's algorithm
def gcd(a,b):
    if b == 0:
        return a;
    else :
        return gcd(b,a%b)

print(gcd(a,b))
