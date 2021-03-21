import math
max_num = 10000
numdict = {}

def sumProperDivisors(num):
    sum = 0
    divisor_list = []
    for i in range(1, int(math.sqrt(num))):
        if num % i == 0:
            divisor_list.append(i)
            j = num/i
            if j == i:
                pass
            elif j == num:
                pass
            else:
                divisor_list.append(int(j))
    #print(num, divisor_list)
    for i in divisor_list:
        sum += i
    return sum

def findAmicables(numdict):
    amicable_list = []
    totsum = 0
    #print(numdict)
    #testdict = {966: 1338, 967: 1, 968: 1027, 969: 471, 970: 794, 971: 1, 972: 1576, 973: 147, 974: 490, 975: 761, 976: 946, 977: 1, 978: 990, 979: 101, 980: 1414, 981: 449, 982: 494, 983: 1, 984: 1536, 985: 203, 986: 634, 987: 549, 988: 972, 989: 67, 990: 1818, 991: 1, 992: 961, 993: 335, 994: 734, 995: 205, 996: 1356, 997: 1, 998: 502, 999: 521}
    for num in numdict:
        if num not in amicable_list:
            #print(num, numdict[num], numdict[numdict[num]])
            sum = numdict[num]
            #print(num, sum)
            try:
                ami = numdict[sum]
                if num == ami and num != sum:
                    print("Pair:", num, sum, numdict[sum])
                    amicable_list.append(numdict[sum])
                    #amicable_list.append(num)
            except:
                pass
                #print("Nope", num, sum)
    #print(amicable_list)
    for i in amicable_list:
        totsum += i
    return totsum

for i in range(1, max_num):
    numdict[i] = int(sumProperDivisors(i))
print("Sum:", findAmicables(numdict))
#print(sumProperDivisors(220))
