from __future__ import annotations

class PowerSum():
    
    def __init__(self, exponent: int, start: int, stop: int) -> None:
        self.exponent = exponent
        self.start = start
        self.stop = stop
        self._sum = 0
        
    def __iter__(self) -> PowerSum:
        self.num = self.start
        return self
    
    def __next__(self) -> int:
        if self.num > self.stop:
            raise StopIteration
        power = self.num ** self.exponent
        self._sum += power
        self.num += 1
        return self._sum
    
if __name__ == "__main__":
    powersum = PowerSum(2,0,3)
    for i in powersum:
        print(i)
        
        
            
            
        