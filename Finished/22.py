alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
totalsum = 0
textfile = open("names.txt", "r")
namelist = textfile.read().replace("\"", "").split(",")
textfile.close()
namelist.sort()
#print(namelist)
for name in namelist:
    sum = 0
    score = 0
    for letter in name:
        #print(letter)
        for char in alphabet:
            #print(char)
            if letter == char:
                sum += alphabet.index(char) + 1
    score = sum * (namelist.index(name) + 1)
    print(name + ":", score)
    totalsum += score
print("Sum of all name scores:", totalsum)
