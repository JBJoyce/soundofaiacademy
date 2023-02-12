from typing import Callable, List

def check_int(func: Callable):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError
        value = func(*args, **kwargs)
        return value
    return wrapper
        
            
def filter_divisble_by(divisor: int):
    def filter_dec(func):
        def wrapper(*args, **kwargs) -> List[int]:
            value = func(*args, **kwargs)
            return [x for x in value if x % divisor == 0]
        return wrapper
    return filter_dec    


@filter_divisble_by(2)
@check_int
def create_squares_list(stop: int) -> List[int]:
    return [n**2 for n in range(stop)]

print(create_squares_list(10))