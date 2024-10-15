# https://leetcode.com/problems/counting-bits/description/?envType=problem-list-v2&envId=rr2ss0g5
# Yes, you can solve this problem in linear time (O(n)) using dynamic programming. The key observation is that the number of 1’s in the binary representation of a number (i) is the same as the number of 1’s in the binary representation of (i/2) (i.e., (i >> 1)), plus 1 if (i) is odd.
# Initialization: 
#    Create an array ans of length (n + 1) initialized to 0.
# Iteration: 
#   For each number (i) from 1 to (n):
#      ans[i >> 1] gives the number of 1’s in the binary representation of (i/2).
#      (i & 1) checks if (i) is odd (i.e., if the least significant bit is 1).
#      Sum these two values to get the number of 1’s in the binary representation of (i).
# This approach ensures that you only pass through the array once, making it (O(n)) in time complexity.
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans




