class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        res,n=0,len(s)
        stack=[]*n
        stack.append(-1)
        for i in range(n):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res=max(res,i-stack[-1])
        return res

            


        