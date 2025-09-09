class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        stack,n,j=list(s),len(s),2
        for i in range(2,len(s)):
            if stack[i]!=stack[j-1] or stack[i]!=stack[j-2]:
                stack[j]=stack[i]
                j+=1
            
        return ''.join(stack[:j])


