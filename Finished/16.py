mystr = str(2**1000)
print(mystr)
mylist = []
for i in mystr:
    mylist.append(i)
sum = 0
print(mylist)
for i in range(0, len(mylist)):
    sum += int(mylist[i])
print(sum)
