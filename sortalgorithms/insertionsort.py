def insertionSort(lst):
    for idx in range(1, len(lst)):
        key = lst[idx]

        while lst[idx - 1] > key and idx > 0:
            lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
            idx -= 1
    return lst

lst = [1, 2, 3, 2, 6, 4, 6, 3, 2, 3, 7, 5]    

print(insertionSort(lst))
