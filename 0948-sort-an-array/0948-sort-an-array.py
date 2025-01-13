class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort/heap sort - 0(nlogn)
        res=[0]*len(nums)

        def merge(l,m,r):
            s1,s2,e1,e2=l,m+1,m-l+1,r-m
            for i in range(e1):
                res[s1+i]=nums[s1+i]
            for i in range(e2):
                res[s2+i]=nums[s2+i]
            i,j,k=0,0,l
            while i<e1 and j<e2:
                if res[s1+i]<=res[s2+j]:
                    nums[k]=res[s1+i]
                    i+=1
                else:
                    nums[k]=res[s2+j]
                    j+=1
                k+=1
            while i<e1:
                nums[k]=res[s1+i]
                i+=1
                k+=1

            while j<e2:
                nums[k]=res[s2+j]
                j+=1
                k+=1


            
        def merge_sort(l,r):
            if l>=r:
                return
            m=l+(r-l)//2
            merge_sort(l,m)
            merge_sort(m+1,r)
            merge(l,m,r)  
        l,r=0,len(nums)-1
        merge_sort(l,r)
        return nums

        
