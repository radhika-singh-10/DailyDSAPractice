class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        freq,n=Counter(nums),len(nums)
        if(n%k!=0):
            return False
        # for k,v in freq.items():
        #     if freq[k]>n//k:
        #         return False
        # return True
        
        return max(list(freq.values()))<=(n//k)
        