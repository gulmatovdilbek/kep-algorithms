n = int(input())
a = list(map(int, input().split()))
min_val = min(a)
index = a.index(min_val) + 1
print(index)