from time import perf_counter_ns

class timer:
    
    def __init__(self) -> None:
        pass
    
    def __enter__(self):
        self.beg = perf_counter_ns()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter_ns()
        self.time = self.end - self.beg
        print(f'Time elapsed = {self.time}')

if __name__ == "__main__":        
    with timer():
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(10):
            print(alphabet[i])
            
            