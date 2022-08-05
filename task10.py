def odd(start, end):
    res = 0
    for i in range(start, end + 1):
        if i <= 1:
            pass
        elif i % 2 != 0:
            res += i
    return res 

print(odd(-5, 10))       