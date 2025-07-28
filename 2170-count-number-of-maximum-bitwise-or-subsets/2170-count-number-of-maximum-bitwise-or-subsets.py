class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        #brute force - recursion - and find subsets and check the max ones and increment the count
        maxOr,res=0,0
        
        for num in nums:
            maxOr|=num

        def backtrack(idx,curOr):
            nonlocal res
            if idx==len(nums) :
                if curOr==maxOr:
                    res+=1
                return 
            #include current number
            backtrack(idx+1,curOr|nums[idx])
            #skip current number
            backtrack(idx+1,curOr)
        backtrack(0,0)
        return res


        