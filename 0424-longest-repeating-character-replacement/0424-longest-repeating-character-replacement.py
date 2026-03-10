class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,res,freq,max_freq=0,0,{},0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            max_freq=max(max_freq,freq[s[r]])
            isValid = (r+1-l-max_freq<=k)
            if not isValid:
                freq[s[l]]-=1
                l+=1
            res=r+1-l
        return res

        #s,k -> sliding window 
        # n=len(s)
        # freq=Counter(s)
        # subStringLen=[0]*n
        # res=0
        # #s=[i for i in s]
        # for l in range(n):
        #     r=l
        #     tempK=k
        #     while tempK>0 and r<n:
        #         if s[r]!=s[l]:
        #             subStringLen[l]=max(subStringLen[l],r-l+1)
        #             tempK-=1
        #         r+=1
        # return res
                
            
                


        