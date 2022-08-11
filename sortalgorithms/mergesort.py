def mergeSort(lst):
    if len(lst) > 1:
        left_arr = lst[:len(lst) // 2]
        right_arr = lst[len(lst) // 2:]

        #recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

        i = 0 # index of left_arr
        j = 0 # index of right_arr
        k = 0 # index of merged array

        # merge
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                lst[k] = left_arr[i]
                i += 1

            else:
                lst[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            lst[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            lst[k] = right_arr[j]
            j += 1
            k += 1
            
    return lst          

lst = [2, 3, 4, 1, 2, 4, 3, 2, 1, 1]

print(mergeSort(lst))
                    

