#Largest Prime Factor
import math

num = 10001

prime_count = 0
i = 2
currnt_prime = 0
while prime_count < num:
    prime = True
    if i == 2:
        current_prime = i
        #print(i)
        prime_count += 1
    elif i % 2 != 0:
        for j in range(2, i):
            if i%j == 0:
                prime = False
                break
        if prime == True:
            current_prime = i
            #print(i)
            prime_count += 1
    i += 1
print(current_prime)
