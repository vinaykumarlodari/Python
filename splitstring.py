def delimPos(passString):
    for eachchar in range(len(passString)):
        if passString[eachchar] == ",":
            x = eachchar
            return x
    
print("Index is:",delimPos("Helloooo,d"))
