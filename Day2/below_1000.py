def some_of_multiples_3_and_5_below_1000():
    return sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])
    
print(some_of_multiples_3_and_5_below_1000())