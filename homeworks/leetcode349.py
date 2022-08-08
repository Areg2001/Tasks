nums1 = [1, 2, 3, 5, 7, 3, 89, 76]
nums2 = [3, 89, 34, 2, 4, 3]
def unique_of_arrays(data1, data2):
    return list(set(nums1) & set(nums2))
    
print(unique_of_arrays(nums1, nums2))    
