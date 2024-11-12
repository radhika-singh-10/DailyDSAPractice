class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True,key=lambda x:x[1])
        res=0
        for i in range(len(boxTypes)):
            if truckSize>=boxTypes[i][0]:
                res+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            else:
                res+=boxTypes[i][1]*truckSize
                break

        return res
            
