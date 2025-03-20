class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,n = 0,len(nums)
        max_len = 0  
        zero_count = 0  
        for r in range(n):  
            if nums[r] == 0:
                zero_count += 1  
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1 
                l += 1  
            max_len = max(max_len, r - l + 1)

        return max_len