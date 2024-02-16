from app.repositories.animal_repo import Animal_repo


class Animal_service:

    def __init__(self):
        self.animal_repo = Animal_repo()

    def get_animals(self):
        animals = self.animal_repo.get_list_animal()
        return [animal.as_dict() for animal in animals]
    
    def search_animal(self, name):
        animals = self.animal_repo.search_animal(name)
        return [animal.as_dict() for animal in animals]

    def update_animal (self, id, animal_data_dto):
        updated_animal = self.animal_repo.update_animal(id, animal_data_dto)
        return updated_animal.as_dict()
    
    def delete_animal(self, id):
        is_deleted = self.animal_repo.delete_animal(id)
        return is_deleted