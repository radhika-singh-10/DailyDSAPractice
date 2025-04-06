class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m,n=len(nums1),len(nums2)
        #we will run loop for m+n times
        #and take maximum no from one array and comapre it with the that index till last of second array and check where it is highest
        #if no hihger element is present in the second array we go for first array and increase i,j by 1 and check from that index till last 
        #this is repeated till k->0
        
        # i,j,count=0,0,0
        # while i<len(m) and j<len(n) and len(res)==k:
        #     max_one,max_two=max(nums1),max(nums2)
        #     if nums1[i]>nums2[j]:
        #         res[count]=nums1[i]
        #         i=i+1
        #     elif nums1[i]<nums2[j]:
        #         res[count]=nums2[j]
        #         j=j+1
        #     else:
        #         res[count]
        #     count+=1
        def getMaxSubSeq(nums,k):
            stack=[]
            for i,num in enumerate(nums):
                while stack and len(nums)-i+len(stack)>k and stack[-1]<num:
                    stack.pop()
                if len(stack)<k:
                    stack.append(num)
            return stack
        
        def merge(nums1,nums2):
            merged=[]
            i,j=0,0
            while i<len(nums1) or j<len(nums2):
                if i>=len(nums1):
                    merged.append(nums2[j])
                    j+=1
                elif j>=len(nums2):
                    merged.append(nums1[i])
                    i+=1
                elif nums1[i:]>nums2[j:]:
                    merged.append(nums1[i])
                    i+=1
                else:
                    merged.append(nums2[j])
                    j+=1
            return merged
        res=[]
        for i in range(max(0,k-len(nums2)),min(len(nums1),k)+1):
            j=k-i
            subSeqOne,subSeqTwo=getMaxSubSeq(nums1,i),getMaxSubSeq(nums2,j)
            merged=merge(subSeqOne,subSeqTwo)
            res=max(res,merged)
        return res

