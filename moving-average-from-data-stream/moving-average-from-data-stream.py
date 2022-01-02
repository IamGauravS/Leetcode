class MovingAverage:

    def __init__(self, size: int):
        self.data = collections.deque()
        self.cursum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.cursum += val
        self.data.append(val)
        if len(self.data) <= self.size:
            return self.cursum/len(self.data)
        movingout = self.data.popleft()
        self.cursum -= movingout
        return self.cursum/self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)