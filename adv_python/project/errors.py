class InvalidCurrencyError(Exception):
    
    def __init__(self, currency: str, message: str) -> None:
        self.currency = currency
        self.message = message