from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class Update_feeding_request(BaseModel):
    name: str = Field( ..., description="Animal name", min_length=3,max_length=50)
    feeding_time: Optional[datetime] = Field(None, description="Feeding time")
    food_count_kg: Optional[int] = Field( None, description="age")
    food_type: str = Field( ..., description="food type", min_length=3,max_length=50)