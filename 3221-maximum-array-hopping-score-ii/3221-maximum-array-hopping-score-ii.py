class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res = 0
        count = 1
        prev = nums[-1]
        for curr in reversed(nums[:-1]):
            if curr>prev:
                res += count*prev
                prev=curr
                count=1
            else:
                count+=1
        res += (count-1)*prev
        return res