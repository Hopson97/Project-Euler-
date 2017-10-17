'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sumOfSquares(sumTo):
    total = 0
    for i in range(sumTo + 1):
        total += (i ** 2)
    return total

def squareOfSums(sumTo):
    total = 0
    for i in range(sumTo + 1):
        total += i
    return total ** 2


if __name__ == "__main__":
    sumTo = 100
    
    result = squareOfSums(sumTo) - sumOfSquares(sumTo)
    print (result)
    