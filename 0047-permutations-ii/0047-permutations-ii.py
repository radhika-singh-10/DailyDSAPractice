class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res,n=[],len(nums)
        def backtrack(index):
            if n==index:
                res.append(nums[:])
                return 
            temp=set()
            for i in range(index,n):
                if nums[i] not in temp:
                    nums[i],nums[index]=nums[index],nums[i]
                    backtrack(index+1)
                    nums[i],nums[index]=nums[index],nums[i]
                    temp.add(nums[i])
            
        backtrack(0)
        return res


    #     res=[]

    #     self.dfs(nums,[],res)
    #     return res

    # def dfs(self,nums,stack,res):
    #     if not nums and not res.__contains__(stack.copy()):
    #         res.append(stack)

    #     for i in range(len(nums)):
    #         self.dfs(nums[:i]+nums[i+1:],stack+[nums[i]],res)