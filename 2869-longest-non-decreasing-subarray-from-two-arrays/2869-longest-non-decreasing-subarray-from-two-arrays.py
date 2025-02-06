class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        #non-decreasing-increasing or equal
        n = len(nums1)
        res = 1
        dp1, dp2 = 1, 1  
        for i in range(1, n):
            new_dp1 = new_dp2 = 1
            if nums1[i] >= nums1[i - 1]:
                new_dp1 = max(new_dp1, dp1 + 1)
            if nums1[i] >= nums2[i - 1]:
                new_dp1 = max(new_dp1, dp2 + 1)
            if nums2[i] >= nums1[i - 1]:
                new_dp2 = max(new_dp2, dp1 + 1)
            if nums2[i] >= nums2[i - 1]:
                new_dp2 = max(new_dp2, dp2 + 1)

            dp1, dp2 = new_dp1, new_dp2
            res = max(res, dp1, dp2)

        return res