def isMultipleof(n, multiple):
    return n % multiple == 0

if __name__ == "__main__":
    sum = 0
    for i in range(1000):
        if isMultipleof(i, 3) or isMultipleof(i, 5):
            sum += i
                
    print(sum)