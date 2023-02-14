from time import perf_counter
from typing import List

def print_time(func):
    def wrapper():
        start = perf_counter()
        func()
        stop = perf_counter()
        print(f'Elapsed time: {stop - start}')
    return wrapper    

@print_time    
def create_one_million_squares_list() -> List[int]:
    return [n**2 for n in range(1000000)]    

if __name__ == "__main__":
    create_one_million_squares_list()