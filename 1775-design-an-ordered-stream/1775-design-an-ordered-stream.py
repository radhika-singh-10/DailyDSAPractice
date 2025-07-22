class OrderedStream:

    def __init__(self, n: int):
        self.store={}
        self.ptr=1

    def insert(self, idKey: int, value: str) -> List[str]:
        store,ptr=self.store,self.ptr
        self.store[idKey]=value
        res=[]
        while ptr in store:
            res.append(store[ptr])
            ptr+=1
        self.ptr=ptr
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)