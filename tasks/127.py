def calculate(a, b):
    s = 0
    for son in range(a, b +1):
        s += son
    return s

print(calculate(1, 5))
print(calculate(5, 7))