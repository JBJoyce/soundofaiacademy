from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union

@dataclass
class EmployeeDTO:

    first_name: str
    last_name: str
    work_email: str
    mobile_number: int
    managers: Union[List[str], List[EmployeeDTO]]
    
    @classmethod
    def from_dict(cls, employee_dict: dict) -> EmployeeDTO:
        return cls(**employee_dict)
    


if __name__ == "__main__":
    employee_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "work_email": "john@company.com",
        "mobile_number": 12345,
        "managers": ["Max", "Frodo"]
    }
    
    employee = EmployeeDTO.from_dict(employee_dict=employee_dict)
    print(employee)