class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff=int((arr[-1]-arr[0])/len(arr))
        res=arr[0]
        
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]!=diff:
                return arr[i-1]+diff

        return res
                


