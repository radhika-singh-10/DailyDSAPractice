class Solution:
    def maximumLength(self, s: str) -> int:
        occurence={}
        for i in range(len(s)):
            ch,substr_len=s[i],0
            for j in range(i,len(s)):
                if ch==s[j]:
                    substr_len+=1
                    occurence[(ch,substr_len)]=(occurence.get((ch,substr_len),0)+1)
                else:
                    break

        res=-1
        for freq in occurence.items():
            length=freq[0][1]
            if freq[1]>=3 and length>res:
                res=length
        return res
                

