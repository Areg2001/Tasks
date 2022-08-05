dict_of_values = {}
lst  = [1, 2, 2, 3, 5, 4, 6, 7, 8, 8, 8, 2, 1]
for i in range(len(lst)):
    dict_of_values[lst[i]] = lst.count(lst[i])
print(dict_of_values)    
