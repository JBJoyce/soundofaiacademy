from abc import ABC, abstractmethod

from project.product import Product


class Transform(ABC):
    ### Interface for concrete Transform which will modify a product object
    
    @abstractmethod
    def apply(product: Product) -> Product:
        ### Apply a transform to a product and return the transformed product
        