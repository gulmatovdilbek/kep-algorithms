# a = float(input("1-sonni kiriting:"))
# b = float(input("2-sonni kiriting:"))

# d = a * a - 4 * b

# x = a + d ** 0.5 /2
# y = a -x

# print(x, y)

import math

def solve():
    a = float(input())
    b = float(input())
    
    discriminant = a ** 2 - 4 * b
    sqrt_d = math.sqrt(discriminant)
    
    x = (a + sqrt_d) / 2
    y = (a - sqrt_d) / 2
    
    print(f"{x} {y}")

solve()