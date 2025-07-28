class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        #brute force - recursion - and find subsets and check the max ones and increment the count
        #memoization - space complexity - worse
        maxOr,res=0,0
        
        for num in nums:
            maxOr|=num

        #memoization
        memo=dict()#[[-1]*(maxoR+1) for _ in range(n)]

        def memoBacktrack(idx, curOr):
            if idx == n:
                return 1 if curOr == maxOr else 0

            if (idx, curOr) in memo:
                return memo[(idx, curOr)]

            without = memoBacktrack(idx + 1, curOr)
            include = memoBacktrack(idx + 1, curOr | nums[idx])

            memo[(idx, curOr)] = without + include
            return memo[(idx, curOr)]

        return memoBacktrack(0, 0)
        #backtracking
        # def backtrack(idx,curOr):
        #     nonlocal res
        #     if idx==len(nums) :
        #         if curOr==maxOr:
        #             res+=1
        #         return 
        #     #include current number
        #     backtrack(idx+1,curOr|nums[idx])
        #     #skip current number
        #     backtrack(idx+1,curOr)
        # backtrack(0,0)
        # return res


        