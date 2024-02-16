from flask import Blueprint, request
from ...utils.database import db
from app.models.animal import Animal
from app.utils.api_response import api_response
from app.services.animal_services import Animal_service
from app.controller.animaldata.Schema.update_animal_req import Update_animal_request

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route('/', methods=["GET"])
def get_list_animal():

    try:

        animal_service = Animal_service()

        animals = animal_service.get_animals()

        return api_response(
            status_code=200,
            message="",
            data=animals
        )
    except Exception as e:
        return str(e), 500
    
@animal_blueprint.route('/<int:animal_id>', methods=["GET"])
def get_animal(animal_id):
        
    try:
        animal = Animal.query.get(animal_id)

        if not animal:
            return "animal not found", 404
        
        return animal.as_dict(), 200
    except Exception as e:
        return str(e), 500
    
@animal_blueprint.route('/search', methods=["GET"])
def search_animal():
        
    try:

        request_data = request.args

        animal_service = Animal_service()

        animals = animal_service.search_animal(request_data["name"])
        return api_response(
            status_code=200,
            message="",
            data=animals
        )
    except Exception as e:
        return str(e), 500
    

@animal_blueprint.route('/', methods=["POST"])
def create_animal():

    try:
        data = request.json
        print(data)
        animal = Animal()
        animal.name = data['name']
        animal.age = data['age']
        animal.species = data['species']        
        animal.gender = data['gender']
        animal.habitat = data['habitat']        
        db.session.add(animal)
        db.session.commit()
        return 'berhasil ditambahkan', 200
    except Exception as e:
        return e, 200
    
@animal_blueprint.route('/<int:animal_id>', methods=["PUT"])
def update_animal(animal_id):

    try:
        
        data = request.json
        update_animal_request = Update_animal_request(**data)

        animal_service = Animal_service()
        animals = animal_service.update_animal(animal_id,update_animal_request)
        
        return api_response(
            status_code=200,
            message="update berhasil",
            data=animals
        )
    except Exception as e:
        return str(e), 500
    
@animal_blueprint.route('/<int:animal_id>', methods=["DELETE"])

def delete_animal(animal_id):
    try:
        animal_service = Animal_service()
        is_deleted = animal_service.delete_animal(animal_id)
        
        if is_deleted:
            return api_response(
                status_code=200,
                message="Data berhasil dihapus",
                data=None
            )
        else:
            return api_response(
                status_code=404,
                message="Data tidak ditemukan",
                data=None
            )
    except Exception as e:
        return str(e), 500