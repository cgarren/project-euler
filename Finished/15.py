import math

grid_size = 40

n=grid_size
r=grid_size/2

def fact(n):
    return math.factorial(n)

c=fact(n)/(fact(r)*fact(n-r))
print(c)
