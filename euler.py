"""This is a library for functions that may be
commonly needed for these solutions.
"""
import math

def isPrime(n):
    """Check for prime, return boolean"""
    n = abs(n)
    isprime = True
    for x in range(2,
            int(math.sqrt(n))+1):
        if n % x == 0:
            isprime = False
            break
    return isprime

def getPrimes(n=1,m=101):
    """Get primes in range n to m"""
    primes = []
    for x in range(n,m):
        if isPrime(x):
            primes.append(x)
    return primes
