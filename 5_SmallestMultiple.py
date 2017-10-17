def isMultipleOf(n, multiple):
    return n % multiple == 0

def testNumber(n):
    for i in range(1, 21, 1):
        if not isMultipleOf(n, i):
            return 
        if i == 20:
            print (n)
            exit()

if __name__ == "__main__":
    n = 0
    while True:
        n += 20
        testNumber(n)
            
            