def sum_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s += raqam

    return s

n = input()
start = n[0:3]
end = n[3:6]
print(sum_digits(start) == sum_digits(end))