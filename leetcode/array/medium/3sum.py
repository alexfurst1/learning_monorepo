# problem 15 - 3sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # why -1 and not +1?
                continue # this skips duplicates once sorted

            l = i + 1
            r = len(nums)-1
            while l > r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    sums.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1 #checks if the l previous l is equal to the last l. 
                    #easier to increment than checking nums[l] == nums[l+1]
                    while l < r and nums[r] == nums[r+1]: r -= 1 #same reasoning, but changed since we decrement r
                elif total > 0:
                    r -= 1  # if the total is positive we know we need a smaller range since nums is sorted, so we help ourselves out here
                else:
                    l += 1
        return sums


  #      -4, -1, 1, 2