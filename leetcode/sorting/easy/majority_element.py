from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        
        max_key = max(counts, key=counts.get)
        return max_key
    
# pretty simple, brute force solution
# haven't figured out the hash map part to make it O(1) yet