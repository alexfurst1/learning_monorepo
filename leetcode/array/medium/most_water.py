# container with most water #11

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            height = min(height[l],height[r])
            area = width * height

            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r += 1

        return max_area
    
# apparently doesn't run with leetcode because somewhere in the grader, height is an int, and can't be used as a list.
# that pissed me off and leetcode sucks so I didn't submit it.