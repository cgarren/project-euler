numdict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
prefixdict = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

def parseHundreds(num):
    return(numdict[int(str(num)[0])] + " hundred")

def parseTens(num):
    if num == 0:
        return ""
    else:
        try:
            return numdict[num]
        except:
            if int(str(num)[0]) == 0: #might be an error here idk
                return numdict[int(str(num)[1])]
            elif int(str(num)[1]) == 0:
                return prefixdict[int(str(num)[0])]
            else:
                return prefixdict[int(str(num)[0])] + "-" + numdict[int(str(num)[1])]
def countCharacters(strnum):
    count = 0
    for i in strnum:
        if i == " " or i == "-":
            pass
        else:
            count += 1
    return count

def returnCount(num):
    if len(str(num)) == 4:
        return countCharacters("one thousand")
    elif len(str(num)) == 3:
        hundreds = parseHundreds(num)
        tens = str(num)[1] + str(num)[2]
        if int(tens) == 0:
            return countCharacters(hundreds)
        elif len(str(int(tens))) == 1:
            return countCharacters(hundreds + " and " + numdict[int(str(num)[2])])
        else:
            strtens = parseTens(int(tens))
            return countCharacters(hundreds + " and " + strtens)
    elif len(str(num)) == 2:
        return countCharacters(parseTens(num))
    elif len(str(num)) == 1:
        return countCharacters(numdict[num])
    else:
        print("Error")

totalcount = 0
for i in range(1, 1001):
    #print(i)
    totalcount += returnCount(i)
print("Sum:", totalcount)
