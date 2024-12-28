class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        def backtrack(index, temp):
            res.append(temp)
            for i in range(index, len(nums)):
                backtrack(i+1,temp+[nums[i]])

        res=[]
        backtrack(0,[])
        return res