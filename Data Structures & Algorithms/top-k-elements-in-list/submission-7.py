from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # Count the occurrences
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Place numbers into frequency buckets
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        # Traverse buckets from high frequency to low
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res