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
        for i in range(len(subset)):
            xor=0
            for j in subset[i]:
                xor^=j
            res+=xor
        return res
                

