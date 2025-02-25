class UndergroundSystem:

    def __init__(self):
        #station dict customer id - [name, time]
        self.station=collections.defaultdict(lambda : [0, 0])

        #name,id = remove by id
        #checkin - startstation ,t (append)
        #checkout - endStation ,

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.station[id]=[stationName,t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,time=self.station.pop(id)
        self.station[(startStation,stationName)][0]+=(t-time)
        self.station[(startStation,stationName)][1]+=1
        # print(self.station)
        # print(self.station[(startStation,stationName)])


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time,trip_count=self.station[(startStation, endStation)]
        return total_time/trip_count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)