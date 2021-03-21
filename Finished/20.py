num = 100

def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

def sumOfDigits(num):
    sum = 0
    num = str(num)
    for i in num:
        sum += int(i)
    return sum

print(sumOfDigits(factorial(num)))
