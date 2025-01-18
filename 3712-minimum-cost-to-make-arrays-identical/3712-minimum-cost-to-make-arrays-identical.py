class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        #sorting pattern , prefixsum
        res,n=0,len(arr)
        ans1,ans2=0,k
        for i in range(n):
            ans1+=abs(arr[i]-brr[i])
        arr.sort()
        brr.sort()
        for i in range(n):
            ans2+=abs(arr[i]-brr[i])
        return min(ans1,ans2)
        