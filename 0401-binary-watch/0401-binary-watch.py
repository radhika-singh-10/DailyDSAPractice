class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        for hr in range(12):
            for mn in range(60):
                if bin(hr).count("1") + bin(mn).count("1")==turnedOn:
                    res.append(f"{hr}:{mn:02d}")
        return res
