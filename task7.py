lst = [2, 5, 1, 6, 4, 9]

def square(n):
    return n ** 2

def sorted_numbers_square(n):
    new = sorted(map(square, lst))
    return list(new)

print(sorted_numbers_square(lst))
