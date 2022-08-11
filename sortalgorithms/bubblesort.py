def bubbleSort(lst):
    for idx in range(len(lst)):
        for j in range(len(lst) - 1 - idx):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst       

lst = [1, 3, 2, 5, 4, 3, 2, 6]         
print(bubbleSort(lst))