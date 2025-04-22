class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #brute n^2
        #optimal - string sorting by hour and min
        #circular loop
        timeData=[]
        for time in timePoints:
            hrs,mins=time.split(":")
            timeData.append(int(hrs)*60+int(mins))
        timeData.sort()
        res=float("inf")
        for i in range(len(timeData)-1):
            res=min(res,abs(timeData[i]-timeData[i+1]))
        return min(res,24*60-timeData[-1]+timeData[0])

