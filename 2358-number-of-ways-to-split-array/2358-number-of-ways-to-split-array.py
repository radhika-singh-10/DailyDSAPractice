class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #edge cases-> 1 element -> 1 split
        #0 ->1 split
        #all unqiue values or any duplicate values?
        #integers only?? or fractions?
        #positive numbers, negative nums, zeroes?
        #can it be sorted or always unsorted? in case of sorted in increasing order->0 for decreasing -> n-1 where n-length of list

        #approach
        #prefix sum can be used here
        #lsum>=rsum; lsum+arr[i]>=rsum
        #calculate the rsum 
        #then lsum+arr[i]>=rsum-arr[i] split+=1
        #else continue
        #tc->0(n) #sc-0(1)
        lsum,rsum=0,0
        n,split=len(nums),0
        for i in range(n):
            rsum+=nums[i]

        for i in range(n-1):
            
            lsum+=nums[i]
            rsum-=nums[i]
            if lsum>=rsum:
                split+=1 
            else:
                continue

        return split
