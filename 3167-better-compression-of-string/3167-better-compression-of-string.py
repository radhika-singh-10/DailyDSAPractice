class Solution:
    def betterCompression(self, compressed: str) -> str:
        #ec1->empty string->emptry string, 
        #ec2->0->not in the string
        #approach->2 pt, iterative
        #hm={}->freq/character
        #this is for mutli digit freq 
        #a10c9 -> if i+1.isdigit() freq*10+(i+1)
        #i,j if i.isalpha() and i+1.isidigit() while not i+1.isdigit():
        # freq=(freq*10)+(i+1) i=i+1 
        #tc->o(n), sp->0(n)
        #for res->traverse the hm in key order and "".join(res)
        if not compressed:
            return compressed
        # if len(s)==1:
        #     return s.join(str(1)) #a -> a1
        hm,i,j,res={},0,0,""
        for i in range(len(compressed)):
            if compressed[i].isalpha():
                j,freq=i+1,0
                while j<len(compressed) and compressed[j].isdigit():
                    freq=freq*10+int(compressed[j])
                    j=j+1
                   
                hm[compressed[i]]=hm.get(compressed[i],0)+freq
        hm=dict(sorted(hm.items()))
        for alphabet in hm:
            res+=alphabet+str(hm[alphabet])
        return res
        


        



        