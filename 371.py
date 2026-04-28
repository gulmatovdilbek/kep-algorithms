n = int(input())
lst = list(map(int, input().split()))
for son  in range(n):
        if lst[son] % 2 == 0: 
           print(lst[son], end = " ")
