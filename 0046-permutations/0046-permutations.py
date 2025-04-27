class Solution:
    #dfs
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.dfs(nums,[],res)
        return res


    def dfs(self,nums,stack,res):
        #print(nums,stack)
        if not nums:
            res.append(stack) 
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],stack+[nums[i]],res)
            

        