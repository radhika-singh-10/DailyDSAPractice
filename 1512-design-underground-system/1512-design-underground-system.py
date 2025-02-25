class UndergroundSystem:

    def __init__(self):
        #station dict customer id - [name, time]
        self.station=collections.defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.station[id]=[stationName,t]


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name,time=self.station.pop(id)
        self.station[(name,stationName)][0]+=(t-time)
        self.station[(name,stationName)][1]+=1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time,trip_count=self.station[(startStation, endStation)]
        return total_time/trip_count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)