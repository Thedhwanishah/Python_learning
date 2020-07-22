"""
Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Example 1:
Input: [3,0,1]
Output: 2
"""
def missingElement(nums):
    # max_element = max(nums)
    max_element = -1
    sum_of_nums = 0
    for i in nums:
        sum_of_nums = sum_of_nums + i
        if i > max_element:
            max_element = i
    total_sum = ((len(nums) + 1) / 2) * (max_element)
    return total_sum - sum_of_nums
array = [9, 6, 4, 2, 3, 5, 7, 0, 1]
result = missingElement(array)
print(result)

