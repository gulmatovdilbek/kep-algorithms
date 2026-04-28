n = int(input())
lst = list(map(int, input().split()))
a = 0
for son in lst:
    if son < 30 and son % 3 == 0:


        print(son, end=" ")
else:
    a += son


print()
print(a)

for index in range(len(lst)):
    print(index, lst[index])