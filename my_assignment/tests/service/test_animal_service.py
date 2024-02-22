from flask import Flask, Response
from app.controller.animaldata.Schema.create_animal_req import Create_animal_request
from app.models.animal import Animal
from app.services.animal_services import Animal_service
from app.repositories.animal_repo import Animal_repo

def test_get_list_animal_success(mocker):

    #Arrange
    mock_animal_data = [
        Animal(
            id=4, 
            name="Cassowari Bird", 
            age=8, 
            gender="Male",
            species="bird",
            habitat="papua"
        ),
        Animal(
            id=6, 
            name="Burung gereja", 
            age=8, 
            gender="Female",
            species="bird",
            habitat="Indonesia"
        ),
    ]
    mocker.patch.object(Animal_repo, 'get_list_animal', return_value=mock_animal_data)

    #Act
    animal_service = Animal_service().get_animals()

    #Assert
    assert len(animal_service) == 2
    assert animal_service[0]['name'] == 'Cassowari Bird'
    assert animal_service[1]['species'] == 'bird'


def test_create_animal_success(test_app, mocker):

    mock_animal_data = Animal(
            id=6, 
            name="Burung gereja", 
            age=8, 
            gender="Female",
            species="bird",
            habitat="Indonesia"
        ),
    mocker.patch.object(Animal_repo, 'create_animal', return_value=mock_animal_data)

    create_dto = Create_animal_request(
            name="Burung gereja", 
            age=8, 
            gender="Female",
            species="bird",
            habitat="Indonesia"
    )


    animal_service_create = test_app.post("/v1/animals/", json=Animal_service().create_animal(create_dto))
    
    assert animal_service_create.json['data']['name'] == "Burung gereja"
    assert animal_service_create.status_code == 201
