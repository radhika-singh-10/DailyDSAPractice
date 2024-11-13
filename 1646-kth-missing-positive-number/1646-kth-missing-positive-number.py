class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_num,count,i=0,0,1
        while count<k:
            if i not in arr:
                missing_num=i
                count+=1
            i+=1

        return missing_num
        
