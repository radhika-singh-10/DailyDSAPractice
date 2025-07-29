class Solution:
    def reorganizeString(self, s: str) -> str:
        freq,n=Counter(s),len(s)
        maxCount,letter=0,''
        for char,count in freq.items():
            if count>maxCount:
                maxCount=count
                letter=char
        if maxCount>(n+1)//2:
            return ""
        res=['']*len(s)
        idx=0
        while freq[letter]!=0:
            res[idx]=letter
            idx+=2
            freq[letter]-=1
        for char,count in freq.items():
            while count>0:
                if idx>=n:
                    idx=1
                res[idx]=char
                idx+=2
                count-=1
        return ''.join(res)

        # freq,n=Counter(s),len(s)
        # res=[0]*n
        # sorted(freq,reverse=True)
        # for i in freq:
        #     j=0
        #     while j<n and freq[i]>0:
        #         res[j]=i
        #         j+=2
        #         freq[i]-=1
        # for i in range(len(res)-1):
        #     if res[i]==res[i+1]:
        #         return ""
        
        # return ""



        # freq=Counter(s)
        # res,l="",0
        # sorted(freq.items(),reverse=True)
        # print(freq)
        # for i in freq:
        #     l+=freq[i]
        
        # for i in freq:
        #     temp_len=freq[i]
        #     while temp_len>0:
        #         res+=i+" "
        #         temp_len-=1
            
        #     # if abs(freq[i]-freq[i+1])!=1:
        #     #     return ""
        #     # else:
        #     #     res+=i
        #     #     res+=i+1
        #     #     freq[i]-=1
        #     #     freq[i+1]-=1
        # return "".join(res)
        # # for i in range(len(s)-1):
        # #     for j in range(i+1,len(s)):
        # #         if s[i]==s[j] and s[j]==s[j+1]:
        # #             return ""
        # #         elif s[i]==s[j] and s[j]!=s[j+1]:
        # #             t=s[j]
        # #             s[j]=s[j+1]
        # #             s[j+1]=t
                
        # # return s