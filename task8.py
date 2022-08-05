def sum_of_digits(n):
    res = 0
    while n != 0:
        res += n % 10
        n = n // 10
    return res

print(sum_of_digits(2345))    
        
        