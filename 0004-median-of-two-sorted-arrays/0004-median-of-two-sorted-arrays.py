class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      #binary search
      #combine the two arrays 
      #total length - l1+l2
        new_arr,p1,p2,res,m,n=[],0,0,0.0,len(nums1),len(nums2)
        while p1<m and p2<n:
            if nums1[p1]<=nums2[p2]:
                new_arr.append(nums1[p1])
                p1+=1
            else:
                new_arr.append(nums2[p2])
                p2+=1
        new_arr.extend(nums1[p1:])
        new_arr.extend(nums2[p2:])
        total_len=len(new_arr)
        if total_len%2==0:
            return (new_arr[(total_len//2)-1]+new_arr[total_len//2])/2
        else:
            return new_arr[total_len//2]

      