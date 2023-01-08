from abc import ABC, abstractmethod


class Animal(ABC):
    
    @abstractmethod
    def make_sound(self) -> None:
        pass
    
    @property
    @abstractmethod
    def number_of_legs(self) -> int:
        pass

class Dog(Animal):

    def make_sound(self) -> None:
        print("woof!")
        
    @property
    def number_of_legs(self) -> int:
        return 4
    
class Duck(Animal):
    
    def make_sound(self) -> None:
        print('quack!')
    
    @property
    def number_of_legs(self) -> int:
        return 2        

if __name__ == "__main__":
    ducky = Duck()
    print(ducky.number_of_legs)
    ducky.make_sound()        
        

    
    