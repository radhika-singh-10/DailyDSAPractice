class Solution:
    def numSub(self, s: str) -> int:
        #sliding window - dynamic window
        l,n,res,mod=0,len(s),0,10**9+7
        for r in range(n):
            if s[r]=='0':
                l=r+1
            res+=(r-l+1)
        
            
        return res%mod

            