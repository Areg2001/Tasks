def SortArrayByParity(nums):
    lst = []
    for i in nums:
        if i % 2 == 0:
            lst = [i] + lst
        else:
            lst += [i]
        
    return lst
    
print(SortArrayByParity([2,5,4,3,2,6,3]))        