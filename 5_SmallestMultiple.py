TESTING_FOR = 20

def isMultipleOf(n, multiple):
    return n % multiple == 0

def testNumber(n):
    for i in range(1, TESTING_FOR + 1, 1):
        if not isMultipleOf(n, i):
            return 
        if i == TESTING_FOR:
            print (n)
            exit()

if __name__ == "__main__":
    n = 0
    while True:
        n += TESTING_FOR
        testNumber(n)
            
            