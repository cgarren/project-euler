#Largest Prime Factor
import math

num_cap = 2000000
prime_list = [3]

i=5
sum = 5
for target in range(i, num_cap+1, 2):
    #print(target)
    index=0
    while prime_list[index] <= math.sqrt(target):
        if target%prime_list[index]==0:
            #print(target, tester, 2)
            break
        index += 1
    else:
        sum += target
        prime_list.append(target)
        #print(target, tester, prime_list)

print("Sum:", sum)
