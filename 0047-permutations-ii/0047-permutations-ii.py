class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]

        self.dfs(nums,[],res)
        return res

    def dfs(self,nums,stack,res):
        if not nums and not res.__contains__(stack.copy()):
            res.append(stack)

        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:],stack+[nums[i]],res)