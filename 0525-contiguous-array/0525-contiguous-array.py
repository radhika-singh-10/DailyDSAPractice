class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res=0
        count=0
        countMap={}
        countMap[0]=-1
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count-=1
            if count in countMap:
                res=max(res,i-countMap[count])
            else:
                countMap[count]=i
        return res
