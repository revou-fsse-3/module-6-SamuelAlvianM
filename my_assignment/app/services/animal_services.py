from app.repositories.animal_repo import Animal_repo
from app.models.animal import Animal


class Animal_service:

    def __init__(self):
        self.animal_repo = Animal_repo()

    def get_animals(self):
        animals = self.animal_repo.get_list_animal()
        return [animal.as_dict() for animal in animals]
    
    def search_animal(self, name):
        animals = self.animal_repo.search_animal(name)
        return [animal.as_dict() for animal in animals]
    
    def create_animal(self, animal_data_dto):
        animal = Animal()

        animal.name = animal_data_dto.name
        animal.age = animal_data_dto.age
        animal.species = animal_data_dto.species        
        animal.gender = animal_data_dto.gender
        animal.habitat = animal_data_dto.habitat

        created_animal = self.animal_repo.create_animal(animal)
        return animal.as_dict()


    def update_animal (self, id, animal_data_dto):
        updated_animal = self.animal_repo.update_animal(id, animal_data_dto)
        return updated_animal.as_dict()
    
    def delete_animal(self, id):
        animal = Animal.query.get(id)
        if not animal:
            return "Data tidak ditemukan"

        is_deleted = self.animal_repo.delete_animal(id)
        return is_deleted.as_dict()