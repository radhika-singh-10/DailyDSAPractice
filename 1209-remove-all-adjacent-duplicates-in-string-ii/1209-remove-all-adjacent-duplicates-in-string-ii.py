class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack,res=[],""
        for i in s:
            if not stack:
                stack.append([i, 1])
            else:
                if i==stack[-1][0]:
                    stack[-1][1]+=1
                else:
                    stack.append([i,1])
            if stack[-1][1]>=k:
                stack[-1][1]-=k
                if stack[-1][1]==0:
                    stack.pop()
        return ''.join([i * j for i, j in stack])




            