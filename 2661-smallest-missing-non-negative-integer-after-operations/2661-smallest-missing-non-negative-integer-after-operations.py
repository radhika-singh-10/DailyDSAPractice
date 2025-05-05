class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n=len(nums)
        #we will get mex in the range of value
        count=Counter(x%value for x in nums)
        minValue=0
        for i in range(value):
            print(i,count[i],minValue,count[minValue])
            if count[i]<count[minValue]:
                minValue=i
        return value*count[minValue]+minValue
              
