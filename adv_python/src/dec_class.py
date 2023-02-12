import time


def wait(seconds: int):
    def wait_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Wait for the magic to happen in {seconds} seconds...")
            time.sleep(seconds)
            func(*args, **kwargs)
        return wrapper
    return wait_decorator

### Note: In a real-world scenario, the “role” should be passed in the constructor, 
### not with a decorator. But I think this is a nice exercise to let you manipulate objects in a decorator. 
def add_role(role: str):
    def add_role_dec(user):
        def wrapper(*args, **kwargs):
            value = user(*args, **kwargs)
            value.role = role
            return value
        return wrapper
    return add_role_dec

@add_role("Admin")
class User:
    
    def __init__(self, name: str) -> None:
        self.name = name
        
    @wait(seconds=3)
    def login(self) -> None:
        print(f"You've been logged in {self.name}")



user = User("Josh")
print(user.role)