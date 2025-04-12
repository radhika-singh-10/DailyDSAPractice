class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        res,heap=[],[]
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while k>0 and heap:
            cur, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return res

        # i1=0
        # j1=range(len(nums1))
        # res=[]
        # for i1 in range(len(nums1)):
        #     temp=[]
        #     for i2 in range(len(nums2)):
        #         if len(res)<k:
        #             temp.append(nums1[i1])
        #             temp.append(nums2[i2])
        #             res.append(temp)
        #         else:
        #             return res
        # return res
