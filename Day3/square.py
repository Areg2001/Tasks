def solution():
    return sum([i ** 2 for i in range(1, 101)]) - sum([i for i in range(1, 101)])
    
print(solution()) 