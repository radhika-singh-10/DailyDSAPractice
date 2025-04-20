class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #similar to koko eating bananas
        #similar to questions asked in mock interview of youtube channel, (keerti purswani)
        #we need to find a balance point as the ships max capacity cant be smaller than max_weight so we check in between max_weight and total_weight
        #


        max_weight,total_weight,res=-1,0,0
        for weight in weights:
            max_weight,total_weight=max(weight,max_weight),total_weight+weight
        left,right=max_weight,total_weight
        #print(left,right)
        while left<right:
            mid=(left+right)//2
            #print(left,right,mid)
            total_day,cur_weight=1,0
            for weight in weights:
                #print(cur_weight,left,right,mid,total_day)
                if cur_weight+weight>mid:
                    total_day+=1
                    cur_weight=0
                cur_weight+=weight
            if total_day>days:
                left=mid+1 
            else:
                right=mid
                
        return left
                


