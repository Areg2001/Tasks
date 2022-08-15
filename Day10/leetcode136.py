def singleNumber(nums):
    for item in nums:
        if nums.count(item) == 1:
            return item

print(singleNumber([1, 3, 2, 3, 1]))
            