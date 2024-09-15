class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res,n=[],len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1] and nums[i] not in res:
                res.append(nums[i])
            
        return res

