# https://leetcode.com/problems/contains-duplicate/description/

# Explanation:
# Initialization: Create an empty set seen to store the elements encountered so far.
# Iteration: Iterate through each element in the array:
# If the element is already in the set, return True (indicating a duplicate).
# Otherwise, add the element to the set.
# Completion: If no duplicates are found by the end of the iteration, return False.
# This approach ensures that you only pass through the array once, making it efficient with a time complexity of (O(n)).

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
