from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i think this is two pointer. I tried using brute force first but couldn't figure out how
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                nums.remove(nums[j])
            else:
                i += 1
                j += 1

        return len(nums)
        
        
# this solution is O(n^2) and only beats 5%. whoops.