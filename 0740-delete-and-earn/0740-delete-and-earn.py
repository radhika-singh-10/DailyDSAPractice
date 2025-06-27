class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        max_points = [0] * (max_number + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])
        
        return max_points[max_number]
        # n,res,i=len(nums),0,1
        # while len(nums)>0:
        #     i=1
        #     #max(nums[i],nums[i-1],nums[i+1])
        #     if len(nums)>2:
        #         num=max(nums[i],nums[i-1],nums[i+1])
        #     elif len(nums)==2:
        #         num=max(nums[i],nums[i-1])
        #     else:
        #         num=nums[0]
        #     res+=num
        #     if num+1 in nums:
        #         nums.remove(num+1)
        #     if num-1 in nums:
        #         nums.remove(num-1)
        #     nums.remove(num)

        # return res


