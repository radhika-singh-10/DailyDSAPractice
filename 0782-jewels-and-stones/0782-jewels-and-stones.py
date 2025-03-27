class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res=0
        stoneMap={}
        for i in range(len(stones)):
            if stones[i] in stoneMap:
                stoneMap[stones[i]]+=1
            else:
                stoneMap[stones[i]]=1
        for k,v in enumerate(stoneMap.items()):
            
            if v[0] in jewels:
               res+=v[1]
            
        return res