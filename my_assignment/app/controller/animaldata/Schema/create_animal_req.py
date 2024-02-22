from pydantic import BaseModel, Field
from typing import Optional

class Create_animal_request(BaseModel):
    name: str = Field( ..., description="Animal name", min_length=3,max_length=50)
    age: Optional[int] = Field( None, description="Animal age")
    species: str = Field( ..., description="Animal's species", min_length=3,max_length=50)
    gender: str = Field( ..., description="gender", min_length=3,max_length=50)
    habitat: str = Field( ..., description="Animal's first born place", min_length=3,max_length=50)


    def as_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'species': self.species,
            'habitat': self.habitat
        }