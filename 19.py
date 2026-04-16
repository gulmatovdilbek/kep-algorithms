n = input()
s = 0

for son in n:
    s += int(son)

print(s)

# n = 4
# sikldagi qadamlar:
# 1. son =1 --> s * 1 = 1
# 2.son =2 --> s * 1 = 1* 2 = 2
# 2.son =3 --> s * 3 = 2* 3 = 6
# 2.son =4 --> s * 4 = 6* 4 = 24