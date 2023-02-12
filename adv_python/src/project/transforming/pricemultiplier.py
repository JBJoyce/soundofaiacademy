from src.project.transforming.transform import Transform
from src.project.product import Product
from src.project.utils import accepts_types


class PriceMultiplier(Transform):
    """Modify the product price attribute by multiplying it by
    a given factor. Concrete implentation of the abstract transform
    class.
    """
    def __init__(self, multiplier: float) -> None:
        self.multiplier = multiplier
    
    @accepts_types(Product)    
    def apply(self, product: Product) -> Product:
        transformed_price = product.price * self.multiplier
        return Product(name=product.name,
                       currency=product.currency,
                       price=transformed_price)
        
            
        