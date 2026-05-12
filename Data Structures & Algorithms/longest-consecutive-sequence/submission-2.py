class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for num in nums:
            if num - 1 in nums: continue # num is not the left most number
            size = 1
            while num + 1 in nums:
                num += 1
                size += 1
            ans = max(ans, size)
        return ans