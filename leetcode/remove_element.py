from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return len(nums)
        
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 0

        return len(nums)
    

# beats 100% in 0 ms. Kindof confused how I nailed it first try but oh well.

#summary:
# pattern: brute force? idk
# edge case: empty 
# gotcha: after doing all these problems this way just felt right and it worked. I don't think theres a gotcha.