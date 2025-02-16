class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #generate subsets
        #compute xor of each subset
        #sum those computation and return 

        if not nums:
            return 0
        res,subset=0,[]
        def subsets(i,temp):
            if i==len(nums):
                subset.append(temp[:])
                return 
            temp.append(nums[i])
            subsets(i+1,temp)
            temp.pop()
            subsets(i+1,temp)
        subsets(0,[])
        print(subset)
        for temp in range(len(subset)):
            xor=0
            for i in subset[temp]:
                xor^=i
            res+=xor
        return res
                

