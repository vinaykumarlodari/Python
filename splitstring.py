def splitString(nuString):
    dp=delimPos(nuString)
    word1 =""
    print(len(nuString))
    for indx in range(len(nuString)):
        if indx < dp :
            word1 = word1 + nuString[indx]
    return word1
    

def delimPos(passString):
    for eachchar in range(len(passString)):
        if passString[eachchar] == ",":
            x = eachchar
            return x
			
print("First Half :",splitString("World is big,Vinay"))

def delimPos(passString):
    for eachchar in range(len(passString)):
        if passString[eachchar] == ",":
            x = eachchar
            return x
    
print("Index is:",delimPos("Helloooo,d"))
