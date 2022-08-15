def missingnumber(nums):
    return ((len(nums)+1) * len(nums) // 2) - sum(nums)

print(missingnumber([0, 1, 3]))