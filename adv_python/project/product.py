from typing import Dict, Any, List

from pydantic import BaseModel, validator

from errors import InvalidCurrencyError

class Product(BaseModel):
    name: str
    price: float
    currencies: Dict[str, List[str]] = {'valid': ['euro', 'dollar']}
    currency: str
    
    @validator('currency')
    @classmethod
    def valid_currency(cls, value: str, values: Dict[str, Any]) -> str:
        if value not in values['currencies']['valid']:
            message = f"Currency: '{value}' isn't supported in product '{values['name']}'."
            raise InvalidCurrencyError(value, message)
        return value
    
    def to_tuple(self) -> tuple:
        return((self.name, self.currency, self.price))

if __name__ == "__main__":
    
    product = Product(name='record', currency='euro', price=12.34)
    print(product.to_tuple())
    
              
    