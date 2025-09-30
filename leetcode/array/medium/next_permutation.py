from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1. Find the first index j (from right) such that nums[j] < nums[j+1]
        j = n - 2
        while j >= 0 and nums[j] >= nums[j + 1]:
            j -= 1

        if j >= 0:  # if such an index exists
            # 2. Find the smallest number greater than nums[j] to the right
            i = n - 1
            while nums[i] <= nums[j]:
                i -= 1
            # 3. Swap them
            nums[j], nums[i] = nums[i], nums[j]

        # 4. Reverse the suffix (everything after j)
        l, r = j + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# this was so annoying and almost made me rethink my career path