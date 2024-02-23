from pydantic import BaseModel, Field
from typing import Optional

class Create_employee_request(BaseModel):
    name: str = Field( ..., description="Employee name", min_length=3,max_length=50)
    age: Optional[int] = Field( None, description="Employee age")
    phone: Optional[int] = Field( None, description="Person age")
    gender: str = Field( ..., description="gender", min_length=3,max_length=50)
    division: str = Field( ..., description="Employee's first born place", min_length=3,max_length=50)


    def as_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'phone': self.phone,
            'division': self.division
        }