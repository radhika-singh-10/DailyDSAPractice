from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.key_value_store=defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.key_value_store:
            self.key_value_store[key]=[]
        self.key_value_store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        val=self.key_value_store.get(key,[])
        l,r=0,len(val)-1
        while l<=r:
            m=l+(r-l)//2
            if val[m][1]<=timestamp:
                l=m+1
                res=str(val[m][0])
            else:
                r=m-1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)