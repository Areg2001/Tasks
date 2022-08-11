def selectionSort(lst):
    for idx in range(len(lst)):
        min_index = idx
        for j in range(idx, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[min_index], lst[idx] = lst[idx], lst[min_index]
    return lst

print(selectionSort([1,2,3,45,1,2,3,5,3,2,2]))