class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l,r=1,max(nums)
         
        def is_possible(max_balls,nums,maxOperations):
            total=0
            for n in nums:
                operations = math.ceil(n/max_balls)-1
                total+=operations
                if total>maxOperations:
                    return False
            return True
            

        while l<r:
            m=(l+r)//2
            if is_possible(m,nums,maxOperations):
                r=m
            else:
                l=m+1
        return l

        
        





