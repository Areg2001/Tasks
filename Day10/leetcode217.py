def containsDuplicate(nums):
    return False if len(nums) == len(set(nums)) else True 

print(containsDuplicate([1, 3, 2, 3, 4]))