from pydantic import BaseModel, Field
from typing import Optional

class Create_animal_report_request(BaseModel):
    name: str = Field( ..., description="your name", min_length=3,max_length=50)
    report_number: Optional[int] = Field( None, description="number from staff given to you")
    report_date: Optional[int] = Field( None, description="date")
    role: str = Field( ..., description="your position", min_length=3,max_length=50)
    explanation: str = Field( ..., description="your comment please", min_length=3,max_length=500)
    
# class Create_visitor_report_request(BaseModel):
#     name: str = Field( ..., description="your name", min_length=3,max_length=50)
#     report_number: Optional[int] = Field( None, description="number from staff given to you")
#     report_date: Optional[int] = Field( None, description="date")
#     type_discussion: str = Field( ..., description="what topics do you want to write", min_length=3,max_length=100)
#     explanation: str = Field( ..., description="your comment please", min_length=3,max_length=500)
    
# class Create_revenue_report_request(BaseModel):
#     name: str = Field( ..., description="your name", min_length=3,max_length=50)
#     report_number: Optional[int] = Field( None, description="number from staff given to you")
#     report_date: Optional[int] = Field( None, description="date")
#     division: str = Field( ..., description="what division", min_length=3,max_length=50)
#     explanation: str = Field( ..., description="write some informations", min_length=3,max_length=500)
#     rev_cal: str = Optional[int]( ..., description="input total calculation of today's profits", min_length=3,max_length=1000)
