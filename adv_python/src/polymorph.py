from abc import ABC, abstractmethod


class Animal(ABC):
    
    @abstractmethod
    def make_sound(self) -> None:
        pass
    
    @property
    @abstractmethod
    def number_of_legs(self) -> int:
        pass

    
    