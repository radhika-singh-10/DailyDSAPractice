class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        
        if i < 0:
            return arr
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        
        while j > 0 and arr[j] == arr[j - 1]:
            j -= 1
        
        arr[i], arr[j] = arr[j], arr[i]
        return arr
        # n,res,maxElem,secondMaxElem,maxIdx,secondMaxIdx=len(arr),[],0,0,0,0
        # #lexicographically largest permutation that is smaller than arr -> with 1 swap
        # #iterate from start, get largest element, find next largest element which is after that largest elem index and replace it
        # for i in range(n):
        #     maxElem=max(maxElem,arr[i])
        # maxIdx=arr.index(maxElem)

        # for i in range(n):
        #     if arr[i]>secondMaxElem and arr[i]!=maxElem and i>maxIdx:
        #         secondMaxElem=arr[i]
        #         secondMaxIdx=i
        # arr[maxIdx],arr[secondMaxIdx]=secondMaxElem,maxElem



        # return arr
