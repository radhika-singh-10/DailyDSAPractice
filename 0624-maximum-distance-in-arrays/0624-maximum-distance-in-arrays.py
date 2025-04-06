class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        #we need to get the min and max value in each scan
        
        min_val,max_val,n,res=arrays[0][0],arrays[0][-1],len(arrays),0
        for i in range(1,n):
            res=max(res,max(abs(arrays[i][-1]-min_val),abs(max_val-arrays[i][0])))
            min_val=min(arrays[i][0],min_val)
            max_val=max(arrays[i][-1],max_val)

        return res


        
            
