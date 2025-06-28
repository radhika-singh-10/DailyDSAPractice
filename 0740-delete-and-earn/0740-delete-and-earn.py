class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        points=defaultdict(int)
        max_num=0
        for num in nums:
            points[num]+=num
            max_num=max(max_num,num)
        max_points = [0] * (max_num+1)
        max_points[1] = points[1]
        for num in range(2,len(max_points)):
            max_points[num]=max(max_points[num-1],max_points[num-2]+points[num])
        return max_points[max_num]
        

        

        
            
        