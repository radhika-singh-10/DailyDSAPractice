class LUPrefix:

    def __init__(self, n: int):
        self.videoList=set()#[0]*(n+1)
        self.longestPrefix=0

    def upload(self, video: int) -> None:
        self.videoList.add(video)
        while self.longestPrefix+1 in self.videoList:
            self.longestPrefix+=1
            
    def longest(self) -> int:
        return self.longestPrefix
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()