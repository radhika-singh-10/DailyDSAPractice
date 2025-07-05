class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n,res=len(arr),-1
        counter=Counter(arr)
        #print(counter)
        for value,count in counter.items():
            if value==count:
                res=max(res,value)
            #print(key,value)
        return res
