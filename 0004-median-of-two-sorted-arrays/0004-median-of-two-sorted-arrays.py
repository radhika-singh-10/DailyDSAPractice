class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #binary search
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            midA = (left + right) // 2
            midB = (m + n + 1) // 2 - midA
            leftA,leftB = (float("-inf") if midA == 0 else nums1[midA - 1]),(float("-inf") if midB == 0 else nums2[midB - 1])
            rightA,rightB = float("inf") if midA == m else nums1[midA],float("inf") if midB == n else nums2[midB]

            if leftA <= rightB and leftB <= rightA:
                if (m + n) % 2 == 0:
                    return (
                        max(leftA, leftB) + min(rightA, rightB)
                    ) / 2
                else:
                    return max(leftA, leftB)
            elif leftA > rightB:
                right = midA - 1
            else:
                left = midA + 1

        #combine the two arrays 
        #total length - l1+l2
        #0(m+n) - below linear method
        # new_arr,p1,p2,res,m,n=[],0,0,0.0,len(nums1),len(nums2)
        # while p1<m and p2<n:
        #     if nums1[p1]<=nums2[p2]:
        #         new_arr.append(nums1[p1])
        #         p1+=1
        #     else:
        #         new_arr.append(nums2[p2])
        #         p2+=1
        # new_arr.extend(nums1[p1:])
        # new_arr.extend(nums2[p2:])
        # total_len=len(new_arr)
        # if total_len%2==0:
        #     return (new_arr[(total_len//2)-1]+new_arr[total_len//2])/2
        # else:
        #     return new_arr[total_len//2]

      