

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        temp = 0
        sum = nums[0] + nums[1] + nums[2]
        

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums)-1
            
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == target:
                    return temp
                elif temp > target:
                    r -= 1
                else:
                    l += 1
                if abs(target - temp) < abs(target - sum):
                    sum = temp
        return sum

                    

                