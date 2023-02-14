from __future__ import annotations
from typing import Union, List, Any, Dict

from pydantic import BaseModel, validator

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
            raise ValueError('Phone number does not contain enough digits')
        return value
    
    @validator('work_email')
    def valid_email(cls, value: str, values: Dict[str, Any]) -> str:
        if not values['first_name'].lower() in value.lower():
            raise ValueError('Work email does not contain employee first name')
        return value
        
if __name__ == "__main__":
    params: dict[str, str | int | list[str]] = {    
        "first_name": "John",
        "last_name": "Doe",
        "work_email": "john@company.com",
        'mobile_number': 12345,
        'managers': ['Max', 'Frodo']
    }
    
    employee_1: EmployeeDTO = EmployeeDTO(
        first_name="John",
        last_name="Doe",
        work_email="john@company.com",
        mobile_number=123456,
        managers=['Max', 'Frodo']
    )
    
    employee_2: EmployeeDTO = EmployeeDTO(**params)
    