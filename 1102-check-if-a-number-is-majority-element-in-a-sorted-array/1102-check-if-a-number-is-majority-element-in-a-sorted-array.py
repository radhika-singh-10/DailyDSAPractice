class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def countElement(nums, l, r, target):
            if l > r:
                return 0
            m = l + (r - l) // 2
            if nums[m] == target:
                return 1 + countElement(nums, l, m - 1, target) + countElement(nums, m + 1, r, target)
            elif nums[m] > target:
                return countElement(nums, l, m - 1, target)
            else:
                return countElement(nums, m + 1, r, target)

        count = countElement(nums, 0, len(nums) - 1, target)
        return count > len(nums) // 2
