class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count,longest_window,l,n=0,0,0,len(nums)
        for r in range(n):
            if nums[r]==0:
                zero_count+=1
            while zero_count>1:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            longest_window=max(longest_window,r-l)

        return longest_window

