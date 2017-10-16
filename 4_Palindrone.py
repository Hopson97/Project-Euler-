#Palindrome Finder#
#the aim of this program is to find the highest palindrome you can get by multiplying 2 3 digit numbers#
def end(number):
    print("Highest Palindrone:", number)
    exit()

def testForPalindrone(number):
    digitList   = str(number)
    listLength  = len(digitList)
    digitBools  = [False] * listLength
    
    for i in range(listLength):
        if (digitList[i] == digitList[listLength - 1 - i]):
            digitBools[i] = True 
    first = digitBools[0]        
    if digitBools.count(first) == listLength and first: #if all elements are the true
        end(number)
    
def main():
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            testForPalindrone(i * j)

main()