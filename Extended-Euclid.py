import math

a  = 63
b  = 42
#Extended-Euclid's algorithm

def EE(x,y):
    if y == 0:
        return (x,1,0);
    else :
        d,a,b = EE(y,x%y)

        return (d,b,a-(math.floor(x/y)*b))

print(EE(a,b))
