from typing import List

from product import Product
from transforming.transform import Transform
from utils import accepts_types



class BatchTransformer:
    """Class that applies multiple transforms to products"""
    
    def __init__(self, transforms: List[Transform]) -> None:
        self._transforms = transforms
        
    @property
    def transforms(self) -> List[Transform]:
        return self._transforms
    
    @transforms.setter
    def transforms(self, transforms: List[Transform]) -> None:
        self._transforms = transforms
        
    @accepts_types(list)
    def apply(self, products: List[Product]) -> List[Product]:
        for transform in self._transforms:
            products = list(map(transform.apply, products))
        return products                      