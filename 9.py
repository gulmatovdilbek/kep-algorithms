# txt = "abcd"
# print(txt[1 : 3]) # bc
# print(txt[0 : 4]) # abcd
# print(txt[0 ::]) # abcd
# print(txt[ :: -1]) # dcba

def reverse_number(num):
    return int(str(num)[::-1])
# print(reverse_number(15889)) # 9851

for number in range(1000, 10000):
    if reverse_number