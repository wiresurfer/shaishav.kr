# https://leetcode.com/problems/two-sum/description/
# To solve this problem efficiently, you can use a hash map to keep track of the indices of the elements you’ve seen so far. This allows you to find the complement of the current element (i.e., target - current element) in constant time. Here’s a Python function to achieve this:
# This function iterates through the list of numbers once, making it efficient with a time complexity of O(n). It uses a hash map to store the indices of the numbers, allowing you to quickly check if the complement of the current number exists in the map.
from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        
