class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            odd,even={},{}
            for j in range(i,len(nums)):
                if nums[j]%2!=0:
                    odd[nums[j]]=odd.get(nums[j],0)+1
                else:
                    even[nums[j]]=even.get(nums[j],0)+1
                
                if len(odd)==len(even):
                    res=max(res,j-i+1)
        return res