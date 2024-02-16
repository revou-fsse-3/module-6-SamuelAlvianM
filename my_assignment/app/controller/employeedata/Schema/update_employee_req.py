from pydantic import BaseModel, Field
from typing import Optional

class Update_employee_request(BaseModel):
    name: str = Field( ..., description="Person name", min_length=3,max_length=50)
    age: Optional[int] = Field( None, description="Person age")
    phone: Optional[int] = Field( None, description="Person age")
    gender: str = Field( ..., description="Person's gender", min_length=3,max_length=50)
    division: str = Field( ..., description="work here as", min_length=3,max_length=50)