def factorials(start: int, stop: int):
    num = start
    _sum = 1
    
    while num <= stop:
        _sum *= num
        yield _sum
        num += 1


if __name__ == "__main__":        
    f = factorials(1, 5)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
          