class Solution:
    def maximumLength(self, s: str) -> int:
        occurence={}
        for i in range(len(s)):
            cur_string=([])
            for j in range(i,len(s)):
                if not cur_string or cur_string[-1]==s[j]:
                    cur_string.append(s[j])
                    cur_to_string="".join(cur_string)
                    if cur_to_string in occurence: 
                        occurence[cur_to_string]+=1
                    else:
                        occurence[cur_to_string]=1
                else:
                    break
        res=0
        for temp_str,freq in occurence.items():
            if freq>=3 and len(temp_str)>res:
                res=len(temp_str)
        if res==0:
            return -1
        return res
                

