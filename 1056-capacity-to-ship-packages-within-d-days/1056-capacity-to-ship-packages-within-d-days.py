class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #similar to koko eating bananas
        #similar to questions asked in mock interview of youtube channel, (keerti purswani)
        #we need to find a balance point
        max_weight,total_weight,res=-1,0,0
        for weight in weights:
            max_weight,total_weight=max(weight,max_weight),total_weight+weight
        left,right=max_weight,total_weight
        while left<right:
            mid=(left+right)//2
            total_day,cur_weight=1,0
            for weight in weights:
                if cur_weight+weight>mid:
                    total_day+=1
                    cur_weight=0
                cur_weight+=weight
            if total_day>days:
                left=mid+1 
            else:
                right=mid
                
        return left
                


