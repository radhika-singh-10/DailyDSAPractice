class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)-1
        i = 0
        j = n 
        sum_list = []
        while i<j:
            k = i +1
            l = j-1
            while k<l:
                s = nums[i]+nums[k]+nums[l]+nums[j]
                if s<target: 
                    k = k+1
                elif s>target:
                    l = l-1 
                else:
                    sum_list.append([nums[i],nums[k],nums[l],nums[j]])
                    k+=1
                    l-=1
                    
     
            i = i+1 
            if i==j:
                i = 0
                j = j-1
                
        
        unique_set = set(map(tuple, sum_list))
        sum_list = list(map(list, unique_set))  
        return sum_list