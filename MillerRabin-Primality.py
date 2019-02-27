# The Miller–Rabin primality test or Rabin–Miller primality test is a primality test
# i.e. an algorithm which determines whether a given number is prime.


# It was first discovered by Russian mathematician M. M. Artjuhov. Gary L. Miller rediscovered it;
# Miller's version of the test is deterministic, but its correctness relies on the unproven extended Riemann hypothesis.
# Michael O. Rabin modified it to obtain an unconditional probabilistic algorithm.


# IsPrime returns "composite" if n is composite and returns "probably prime" if n
# is probably prime.  k is an input parameter that determines
# accuracy level. Higher value of k indicates more accuracy.


import math
import random

def isPrime(n,k):
    r = 0
    if n <= 1:
        return "composite"
    elif n == 2 or n == 3:
        return "probably prime"
    elif n%2 == 0:
        return "composite"
    else:
        a = n-1
        while(a%2 == 0):
            a = a/2
            r += 1
        d = int((n-1)/(2**r))

        arr = []
        for i in range(0,k):
            u = primalityRabinMiller(n,d)
            arr.append(u)
        print(arr)

        faith = 0
        for i in arr:
            faith = faith + i
        print(faith)
        if faith/k >= 0.5:             # Voting and averaging to find what most of tests agree on i.e. prime or composite
            return "probably prime"
        else: return "composite"

seed = 42
random.seed(seed)                      # setting the seed to generate random numbers






def primalityRabinMiller(n,d):         # Miller Rabin Primality test

    a = random.randrange(2,n-2)

    x = (a**d) % n                     # Compute: x = pow(a, d) % n
    if x==1 or x == n-1:
        return 1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return 0
        if (x == n - 1):
            return 1

    return 0






if __name__ == "__main__":
    p = int(input("Enter the number : "))
    k = int(input("Enter the no. of accuracy tests : "))  # k is an input parameter that determines accuracy level.
                                                          # Higher value of k indicates more accuracy.

    print(isPrime(p,k))
