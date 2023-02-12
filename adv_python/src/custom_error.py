from __future__ import annotations
from typing import Union, List, Any, Dict

from pydantic import BaseModel, validator

class TooFewDigitsError(Exception):
    
    def __init__(self, number: int, message: str) -> None:
        self.number= number,
        self.message= message
        
class FirstNameNotInWorkEmailError(Exception):
    
    def __init__(self, work_email: str, first_name: str, message: str) -> None:
        self.work_email = work_email,
        self.first_name = first_name,
        self.message = message
                
class EmployeeDTO(BaseModel):

    first_name: str
    last_name: str
    work_email: str
    mobile_number: int
    managers: Union[List[str], List[EmployeeDTO]]
    complete_name: str = None
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.complete_name = f'{self.first_name} {self.last_name}'
    
    @validator('mobile_number')
    def valid_phone_number(cls, value: int) -> int:
        if len(str(value)) < 6:
            msg = 'Phone number does not contain enough digits'
            raise TooFewDigitsError(value, msg)
        return value
    
    @validator('work_email')
    def valid_email(cls, value: str, values: Dict[str, Any]) -> str:
        if not values['first_name'].lower() in value.lower():
            msg = 'Work email does not contain employee first name'
            raise FirstNameNotInWorkEmailError(value, values['first_name'], msg)
        return value
        
if __name__ == "__main__":
    params: dict = {    
        "first_name": "John",
        "last_name": "Doe",
        "work_email": "jane@company.com",
        'mobile_number': 123456,
        'managers': ['Max', 'Frodo']
    }
    
    employee_1: EmployeeDTO = EmployeeDTO(
        first_name="John",
        last_name="Doe",
        work_email="jane@company.com",
        mobile_number=123456,
        managers=['Max', 'Frodo']
    )
    
    employee_2: EmployeeDTO = EmployeeDTO(**params)
    