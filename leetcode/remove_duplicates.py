from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                     # empty list → nothing to do
            return 0
        
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

# summary:
# pattern: two pointer (sliding window?)
# edge case: empty list
# gotcha: realizing I can't use for loops because they don't work well when changing the length of the list they loop over