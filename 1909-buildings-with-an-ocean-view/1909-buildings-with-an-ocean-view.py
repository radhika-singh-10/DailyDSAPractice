class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #approach -> i-0-n-1, j-i+1,n if arr[i]<arr[j] break else continue and apprend the index to res if i==n-1 subcessfully
        if len(heights)==0:
            return []
        elif len(heights)==1:
            return [0]
        else:
            res=[]
            max_height=0
            for i in range(len(heights) - 1, -1, -1):
                if heights[i] > max_height:  
                    res.append(i)
                    max_height = heights[i]
            return res[::-1]