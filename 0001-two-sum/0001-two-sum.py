class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res={}
        for i,j in enumerate(nums):
            c=target-j
            if c in res:
                return [res[c],i]

            res[j]=i
        return res