class Solution:
    def twoSum(self, nums:[1,2,3,4], target: 5) -> List[int]:
        priv={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in priv:
                return [priv[diff],i]
            priv[n]=i
        return 
        