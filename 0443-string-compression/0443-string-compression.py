class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        res,n,w,r=0,len(chars),0,0
        # if n==0:
        #     return 0
        while r<n:
            ch,count=chars[r],0
            while r<n and chars[r]==ch:
                r+=1
                count+=1
            
            chars[w]=ch
            w+=1
            if count>1:
                for d in str(count):
                    chars[w]=d
                    w+=1
        return w
            
        