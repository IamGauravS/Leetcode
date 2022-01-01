from collections import deque
class HitCounter:

    def __init__(self):
        self.queueobject = deque()

    def hit(self, timestamp: int) -> None:
        if self.queueobject and self.queueobject[-1][0] == timestamp:
            self.queueobject[-1][1] += 1
        else:
                while self.queueobject and timestamp - self.queueobject[0][0] >= 300:
                    self.queueobject.popleft()
                    
                self.queueobject.append([timestamp, 1])
                    

    def getHits(self, timestamp: int) -> int:
        sum = 0
        while self.queueobject and timestamp - self.queueobject[0][0] >= 300:
            self.queueobject.popleft()
            
        for elem in self.queueobject:
            sum += elem[1]
            
        return sum


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)