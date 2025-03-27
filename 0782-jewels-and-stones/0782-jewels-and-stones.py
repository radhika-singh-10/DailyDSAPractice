class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res=0
        jewels=set([j for j in jewels])
        for s in stones:
            if s in jewels:
                res+=1

        return res
        # stoneMap={}
        # for i in range(len(stones)):
        #     if stones[i] in stoneMap:
        #         stoneMap[stones[i]]+=1
        #     else:
        #         stoneMap[stones[i]]=1
        # for k,v in enumerate(stoneMap.items()):
            
        #     if v[0] in jewels:
        #        res+=v[1]
            
        # return res