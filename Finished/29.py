mylist = []
topint = 100
for i in range(2,topint+1):
    for j in range(2,topint+1):
        num = i**j
        if num not in mylist:
            mylist.append(num)
print(len(mylist))
