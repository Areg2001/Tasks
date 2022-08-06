def iseven(n):
    return n % 2 == 0
    
def fib(n):
    list_of_fib_numbers = []
    first, second, nextItem = 0, 1, 0
    while nextItem <= n:
        nextItem = first + second
        first = second
        second = nextItem
        print(nextItem)
        if iseven(nextItem):
            if nextItem <= n:
                list_of_fib_numbers.append(nextItem)
    return sum(list_of_fib_numbers)

print(fib(4000000))    