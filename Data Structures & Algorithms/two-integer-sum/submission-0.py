class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        priv={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in priv:
                return [priv[diff],i]
            priv[n]=i
        return 
        