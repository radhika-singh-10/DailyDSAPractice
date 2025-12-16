class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n,res=len(nums),0
        max_val,min_increment=max(nums),0
        freq_count=[0]*(n+max_val)
        for val in nums:
            freq_count[val]+=1
        for i in range(len(freq_count)):
            if freq_count[i]<=1:
                continue
            duplicates=freq_count[i]-1
            freq_count[i+1]+=duplicates
            freq_count[i]=1
            min_increment+=duplicates
        return min_increment