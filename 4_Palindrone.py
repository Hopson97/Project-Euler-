#Palindrome Finder#
#the aim of this program is to find the highest palindrome you can get by multiplying 2 3 digit numbers#
 
highest = 0
itr = 0
isPal = False

for x in range(999, 0, -1):
    for y in range(999, 0, -1):
        itr += 1
        total = x * y
        nList = list(str(total))
        
        length  = len(nList)
        pals     = [False] * length #one boolean per digit
        for i in range (length):
            if (nList[i] == nList[length - 1 - i]): #if the number either side is the same, set the bool to true
                pals[i] = True
        
        #test if the whole list of bools is true
        isPal = True
        for bool in pals:
            if not bool:
                isPal = False
                break
            else:
                isPal = True
                
        if isPal:
            if total > highest:
                highest = total
                
        if isPal:
            break
    if isPal:
        break
                
        
                
print ("result:", highest, "took", itr, "iterations to find")