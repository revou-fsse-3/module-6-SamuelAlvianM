from app.services.animal_services import Animal_service


def test_get_animal(test_app, mocker):
# Arrange
    mock_animal_data = [
        {
            "id": 4,
            "name": "Cassowari Bird",
            "age": 8,
            "gender": "Female",
            "habitat": "papua",

        },
    ]
    mocker.patch.object(Animal_service, 'get_animals', return_value=mock_animal_data)

    #Act
    response = test_app.get("/v1/animals/")

    assert response.status_code == 200
    assert response.json['data'] == mock_animal_data
    assert len(response.json['data']) == len(mock_animal_data)

#  test untuk post data animal request

def test_post_animal(test_app, mocker):
    #Arrange
    data = {
        "name": "Frostallion",
        "age": 8,
        "species": "Nocht",
        "gender": "male",
        "habitat": "mount everest",
    }
    mocker.patch.object(Animal_service, 'create_animal', return_value=data)

    #Act
    response = test_app.post("/v1/animals/", json=data)

    #Assert
    assert response.status_code == 201
    assert response.json['data']["name"] == "Frostallion"

def test_put_animal(test_app, mocker):
    # ARRANGE
    data ={
        "age": 8,
        "gender": "male",
        "habitat": "mount everest",
        "name": "Frostallion",
        "species": "Nocht"
    }
    mocker.patch.object(Animal_service, 'update_animal', return_value=data)

    # ACT
    response = test_app.put("/v1/animals/3", json=data)

    # ASSERT
    assert response.status_code == 200

def test_put_animal_code_400(test_app, mocker):
    
    data ={}

    mocker.patch.object(Animal_service, 'update_animal', return_value=data)
    response = test_app.put("/v1/animals/", json=data)
    assert response.status_code == 405


def test_delete_animal_not_found(test_app, mocker):
    #Arrange
    expected_response = "Data tidak ditemukan"
    
    mocker.patch.object(Animal_service, "delete_animal", return_value=expected_response)

    #Act
    response = test_app.delete("/v1/animals/222")

    #Assert
    assert response.status_code == 404


def test_delete_animal (test_app, mocker):

    expected_response = {
        "data": None,
        "status": {
            "code": 200,
            "message": "Data Berhasil Dihapus"
        }
    }

    mocker.patch.object(Animal_service, "delete_animal", return_value=expected_response)

    response = test_app.delete("/v1/animals/3")

    assert response.status_code == 200

def test_search_animal_by_id(test_app, mocker):

    expected_data =  [
        {
            "age": 8,
            "gender": "male",
            "habitat": "mount everest",
            "id": 3,
            "name": "Frostallion",
            "species": "Nocht",
        }
    ]
    
    expected_response = {
        'data': expected_data,
        'status': {
            "code": 200,
            "message": "ini yang kamu cari?"
        }
    }


    mocker.patch.object(Animal_service, 'search_animal', return_value=expected_response)

    # ACT
    response = test_app.get("/v1/animals/search?name=Frostallion")

    # ASSERT
    assert response.status_code == 200
    assert response.json['data'] == expected_response


