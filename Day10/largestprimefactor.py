def isPrime(n):
    for i in range(3, n):
        if n % i == 0:
            return False

    return True

def largestPrimeFactor():
    n = 600851475143
    prime = 3
    while n != 1:
        if isPrime(prime):
            if n % prime == 0:
                n = n // prime
        prime += 1
    return prime - 1  

print(largestPrimeFactor())
