class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #edge cases-> no elements-> [[]], integers/fractions?, +ve, 0, -ve nos.
        #for fractions-> to check for single no subset-> need to take ceil or floor or like that only??

        #backtracking approach
        #two pointers - 0-i, i-n-1 , n=len(nums)
        #sort the elements to know if that element is present or not
        #run the loop- i=0-n -> 
        #we check if the element is same as prev then cintinue else append in the new list, i=i+1
        #0(2^n) 0(n^2)
        
        res=[]
        if not nums:
            return res
        n=len(nums)
        nums.sort()
        def backtrack(nums,res,index,temp):
            res.append(temp.copy())
            for i in range(index,n):
                #print(i,index)
                if i!=index and  nums[i-1]==nums[i]:
                    continue
                    
                temp.append(nums[i])
                backtrack(nums,res,i+1,temp)
                temp.pop()


        backtrack(nums,res,0,[])
        return res
