'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def isEven(num):
    return num % 2 == 0

#DOES NOT WORK YET
if __name__ == "__main__":
    sequence = []
    a = 1 
    b = 2
    while a < 4000000 and b < 4000000:
        if isEven(a):
            sequence.append(a)
        if isEven(b):
            sequence.append(b)
        a = a + b
        b = a + b 
        
    print(sequence)
    sum = 0
    for i in sequence:
        sum += i
    print ("\nSum: ", sum)
        
        
        
        
        
        