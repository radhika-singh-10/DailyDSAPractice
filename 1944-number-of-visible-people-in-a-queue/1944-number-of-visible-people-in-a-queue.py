class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        res = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                res[i] += 1
            if stack:
                res[i] += 1
            stack.append(heights[i])
        return res
        # n=len(heights)
        # res=[0]*n
        # stack=[]
        # for idx,val in enumerate(heights):
        #     while stack and heights[stack[-1]]<=val:
        #         res[stack.pop()]+=1
        #     if stack:
        #         res[stack[-1]]+=1
        #     print(stack,idx)
        #     stack.append(idx)
        # return res
        
        