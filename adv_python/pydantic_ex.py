from __future__ import annotations
from typing import List, Union

from pydantic import BaseModel

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
        mobile_number=12345,
        managers=['Max', 'Frodo']
    )
    
    employee_2: EmployeeDTO = EmployeeDTO(**params)
    
    print(employee_1 == employee_2)
    print(employee_1.complete_name)