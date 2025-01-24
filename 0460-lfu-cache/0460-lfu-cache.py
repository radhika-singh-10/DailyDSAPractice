from collections import OrderedDict, defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        # self.capacity=capacity
        # self.cache=OrderedDict([])
        # self.minFreq=0
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = collections.defaultdict(collections.OrderedDict)
        self.minf = 0

    def get(self, key: int) -> int:
        # if key not in self.cache:
        #     return -1
        # oldFreq=self.cache[key][1]
        # self.cache[key][1]+=1
        # self.cache[oldFreq].pop(key)
        # if not self.cache[key][1]==oldFreq:
        #     del self.cache[key]
        # self.cache[key][oldFreq+1][2]=1
        # if self.minFreq not in self.cache:
        #     self.minFreq+=1
        # return self.cache[key][0]

        if key not in self.key2val:
            return -1
        oldfreq = self.key2freq[key]
        self.key2freq[key] = oldfreq + 1
        self.freq2key[oldfreq].pop(key)
        if not self.freq2key[oldfreq]:
            del self.freq2key[oldfreq]
        self.freq2key[oldfreq + 1][key] = 1
        if self.minf not in self.freq2key:
            self.minf += 1
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        # if self.capacity<=0:
        #     return 
        # if key in self.cache:
        #     self.cache.get(key)
        #     self.cache[key][0]=value
        # if len(self.cache)==self.capacity:
        #     delkey,_=self.cache[self.minFreq].popitem(last=False)
        #     del self.cache[delkey]
        # self.cache[key][0],self.cache[key][1],self.cache[key][2]=value,1,1
        # self.minFreq=1

        if self.cap <= 0:
            return
        if key in self.key2val:
            self.get(key)
            self.key2val[key] = value
            return

        if len(self.key2val) == self.cap:
            delkey, _ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.minf = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)