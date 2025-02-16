class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[i for i in range(1,10)]
        res=set()
        #
        #backtracking
        #check if nums[i]+total==k: append in res and return 
        #if i==len(nums) or total>k:return
        #temp.append(nums[i]) 
        #total+=nums[i]
        #backtrack_subset(i,total+nums[i],temp)
        #temp.pop()
        #backtrack_subset(i,total,temp)

        def backtrack_subset(i,total,temp):
            if len(temp) == k and total == n:
                    res.add(tuple(temp[:]))
                    return

            for i in range(i,10):
                if total+i>n:
                    return 

                temp.append(i) 
                backtrack_subset(i+1,total+i,temp)
                temp.pop()
                
            
            # temp.append(nums[i]) 
            # #total+=nums[i]
            # backtrack_subset(i+1,total+nums[i],temp)
            # temp.pop()
            # backtrack_subset(i+1,total,temp)

        backtrack_subset(1,0,[])

        return [combination for combination in res]