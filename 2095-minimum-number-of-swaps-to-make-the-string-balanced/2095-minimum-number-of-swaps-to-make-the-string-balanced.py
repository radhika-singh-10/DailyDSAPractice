class Solution:
    def minSwaps(self, s: str) -> int:
        n,openBrackets=len(s),0
        #2pointer-maxswaps-n/2 -> (0-n//2) 
        
        #no of (open brackets that are unbalanced+1)/2 -> make minimum
        for c in s:
            if c=='[':
                openBrackets+=1
            else:
                if openBrackets>0:
                    openBrackets-=1
        return (openBrackets+1)//2



        
        # stack=[i for i in s]
        # l,r,res=0,len(s)-1,0
        # while l<r:
        #     if stack[l]=='[' or (stack[l]=='[' and stack[r]=='['):
        #         l+=1
        #     elif stack[r]==']' or (stack[l]==']' and stack[r]==']'):
        #         r-=1
        #     elif stack[l]==']' and stack[r]=='[':
        #         stack[l],stack[r]=stack[r],stack[l]
        #         l+=1
        #         r-=1
        #         res+=1
        # return res

        
           

