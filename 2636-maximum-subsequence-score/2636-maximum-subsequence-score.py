class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # sort accoridng to 2nd array
        # [(3,1),(1,2),(3,3),(2,4)]
        # perform top down 
        n,combined_nums=len(nums1),[(a,b) for a,b in zip(nums1,nums2)]
        combined_nums.sort(key=lambda x:-x[1])
        top_k_elements=[x[0] for x in combined_nums[:k]]
        top_k_sum=sum(top_k_elements)
        heapq.heapify(top_k_elements)
        res=top_k_sum*combined_nums[k-1][1]
        for i in range(k,len(nums1)):
            top_k_sum-=heapq.heappop(top_k_elements)
            top_k_sum+=combined_nums[i][0]
            heapq.heappush(top_k_elements,combined_nums[i][0])
            res=max(res,top_k_sum*combined_nums[i][1])
        return res
        
        
