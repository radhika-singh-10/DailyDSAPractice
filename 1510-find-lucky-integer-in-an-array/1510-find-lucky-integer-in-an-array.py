class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n,res=len(arr),-1
        counter=Counter(arr)
        #print(counter)
        for key,value in enumerate(counter):
            if value==counter[value]:
                res=max(res,value)
            #print(key,value)
        return res
