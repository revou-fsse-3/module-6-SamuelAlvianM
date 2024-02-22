from flask import Blueprint, request
from pydantic import ValidationError
from app.controller.animaldata.Schema.create_animal_req import Create_animal_request
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
            message="ini yang kamu cari?",
            data=animals
        )
    except Exception as e:
        return str(e), 500
    

@animal_blueprint.route('/', methods=["POST"])
def create_animal():

    try:
        data = request.json
        update_animal_request = Create_animal_request(**data)

        animal_service = Animal_service()

        animals = animal_service.create_animal(update_animal_request)

        return api_response(
            status_code=201,
            message="berhasil ditambahkan",
            data= animals
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
    
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
        
        if is_deleted == "Data tidak ditemukan":
            return api_response(
                status_code=404,
                message=is_deleted,
                data="none"
            )
        
        return api_response(
                status_code=200,
                message="Data Berhasil dihapus",
                data=is_deleted
            )
    except Exception as e:
        return api_response(
            status_code=500,
            message = str(e),
            data={}
        )