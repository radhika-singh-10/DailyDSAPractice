class Solution:
    def candy(self, ratings: List[int]) -> int:
        n,res=len(ratings),0
        candies_left,candies_right=[1]*n,[1]*n
        for i in range(1,n):
            if ratings[i-1]<ratings[i]:
                candies_left[i]=candies_left[i-1]+1

        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                candies_right[i]=candies_right[i+1]+1

        for i in range(n):
            res+=max(candies_left[i],candies_right[i])
        
        return res
        