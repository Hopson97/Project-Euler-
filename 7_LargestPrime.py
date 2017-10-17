'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def isPrime(a):
    return all(a % i for i in range(2, a))

if __name__ == "__main__":
    primes = []
    n = 2
    while len(primes) != 10001:
        if (isPrime(n)):
            primes.append(n)
        n += 1
    
    print(primes[-1])
    