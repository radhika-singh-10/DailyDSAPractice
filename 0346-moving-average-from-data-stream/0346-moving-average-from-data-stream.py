class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.ls=[]

    def next(self, val: int) -> float:
        if len(self.ls)<self.size:
            self.ls.append(val)
        else:
            el=self.ls.pop(0)
            self.ls.append(val)

        return sum(self.ls)/len(self.ls)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)