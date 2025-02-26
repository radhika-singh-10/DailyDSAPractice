class Solution:
    def findScore(self, nums: List[int]) -> int:
        score,i,n=0,0,len(nums)
        sorted_nums=[(num,index) for index,num in enumerate(nums)]
        sorted_nums.sort()
        marked=[False]*n
        for i in range(n):
            num,j=sorted_nums[i][0],sorted_nums[i][1]
            if not marked[j]:
                score+=num
                marked[j]=True
                if j-1>=0:
                    marked[j-1]=True
                if j+1<n:
                    marked[j+1]=True
        return score

        return score

