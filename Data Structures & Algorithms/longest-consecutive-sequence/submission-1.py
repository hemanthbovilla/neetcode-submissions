class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        store=set(nums)
        for num in nums:
            streak,crr=0,num
            while crr in store:
                streak+=1
                crr+=1
            res=max(res,streak)
        return res