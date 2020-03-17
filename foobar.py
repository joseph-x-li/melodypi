import math

def isPrime(n):
    if n%2==0 and n != 2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True
    
def generatePrimes(goalLen):
    primes = ""
    counter = 2
    while(len(primes) < goalLen + 7):
        if isPrime(counter):
            primes += str(counter)
        counter += 1
    return primes
    
def solution(i):
    return generatePrimes(i)[i:i+5]