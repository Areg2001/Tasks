def sum_of_digits(n):
    res = 0
    while n != 0:
        res += n % 10
        n = n // 10
    return res    

def product_of_digits(n):
    res = 1
    while n != 0:
        res *= n % 10
        n = n // 10
    return res

def difference_of_product_and_sum_of_digits(n):
    return product_of_digits(n) - sum_of_digits(n)

print(difference_of_product_and_sum_of_digits(234))            