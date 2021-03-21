from functools import reduce

max_factors = 0
current_num = 0
c = 1

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while max_factors <= 500:
    #Generate next triangle number
    current_num += c

    #Find divisors of the number
    divisor_list = factors(current_num)
    # for i in range(1, current_num+1):
    #     if i not in divisor_list:
    #         if current_num%i==0:
    #             #print(current_num, i)
    #             divisor_list.append(i)
    #input("")
    if len(divisor_list) > max_factors:
        max_factors = len(divisor_list)
    #print(current_num, len(divisor_list))
    c += 1


print(current_num, "has", max_factors, "factors")
