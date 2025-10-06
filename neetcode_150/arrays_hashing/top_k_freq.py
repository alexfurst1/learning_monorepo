from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        top_k = [key for key, val in (sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k])]

        return top_k