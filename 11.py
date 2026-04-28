def is_prime(n):
    if n <= 1:
        return False
# n = 15; 2, 3, 4, ... 14  
    for son in range(2, n):
        if n % son == 0:
            return False
        
    return True

n = int(input())
print("Yes") if is_prime(n) else print("No")