class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
        l,r=0,len(s)-1
        prefix,suffix=[],[]
        while l<r and s[l]==s[r]:
            # prefix.append(s[l])
            # suffix.append(s[r])
            ch=s[l]
            while l<=r and ch==s[l]:
                l+=1
            
            while r>l and ch==s[r]:
                r-=1
            
        return r-l+1
        
        
        
            
            
