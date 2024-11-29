from collections import deque
class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        # self.cache={} #to get the frequency stored as key-value
        # self.order=deque()#to get the order 
        self.cache=collections.OrderedDict()

    def get(self, key: int) -> int:
        #if key is present, we move the most recently accessed to the last
        if key in self.cache:
            # self.order.remove(key)
            # self.order.append(key)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists, we update the value and move it to the end of the cache, then we check If capacity is exceeded, we remove the least recently used key
        if key in self.cache:
            self.cache.move_to_end(key)
            #self.order.remove(key)
        # elif len(self.cache) >= self.capacity:
        #     lru_key = self.order.popleft()
        #     del self.cache[lru_key]
       
        self.cache[key] = value
        if len(self.cache)>self.capacity:
            self.cache.popitem(False)
        # self.order.append(key)
        # print(self.cache,self.order)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)