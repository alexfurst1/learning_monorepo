from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)
        if len(new_set) != len(nums):
            return True
        else:
            return False