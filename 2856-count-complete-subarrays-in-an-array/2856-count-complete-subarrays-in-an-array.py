class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count,n,res,temp_count,r=len(set(nums)),len(nums),0,{},0
        #sliding windows
        for l in range(n):
            #print(temp_count,l,r)
            if l>0:
                temp_count[nums[l-1]]-=1
                if temp_count[nums[l-1]]==0:
                    temp_count.pop(nums[l-1])
            while r<n and len(temp_count)<distinct_count:
                temp_count[nums[r]]=temp_count.get(nums[r],0)+1
                r=r+1
                #print(temp_count,l,r)
            if len(temp_count)==distinct_count:
                res+=n-r+1
                
                #print(temp_count,l,r)
        return res
            
