from app.services.employee_services import Employee_service


def test_get_employee(test_app, mocker):
# Arrange
    mock_employee_data = [
        {
            "age": 17,
            "division": "manager",
            "gender": "male",
            "name": "jean",
            "phone": 777
        }
    ]
    mocker.patch.object(Employee_service, 'get_Employees', return_value=mock_employee_data)

    #Act
    response = test_app.get("/v1/employee/")

    assert response.status_code == 200
    assert response.json['data'] == mock_employee_data
    assert len(response.json['data']) == len(mock_employee_data)


def test_post_employee(test_app, mocker):
    #Arrange
    data =  {
        "age": 17,
        "division": "manager",
        "gender": "male",
        "name": "jean",
        "phone": 777
    }

    mocker.patch.object(Employee_service, 'create_employee', return_value=data)

    #Act
    response = test_app.post("/v1/employee/", json=data)

    #Assert
    assert response.status_code == 201
    assert response.json['data']["name"] == "jean"

def test_put_employee(test_app, mocker):
    # ARRANGE
    data ={
        "age": 19,
        "division": "Software Engineer Senior",
        "gender": "male",
        "name": "Kevin",
        "phone": 777
    }

    mocker.patch.object(Employee_service, 'update_Employee', return_value=data)

    # ACT
    response = test_app.put("/v1/employee/3", json=data)

    # ASSERT
    assert response.status_code == 200

def test_put_employee_code_400(test_app, mocker):
    
    data ={}

    mocker.patch.object(Employee_service, 'update_Employee', return_value=data)
    response = test_app.put("/v1/employee/", json=data)
    assert response.status_code == 405


def test_delete_employee_not_found(test_app, mocker):
    #Arrange
    expected_response = "Data tidak ditemukan"
    
    mocker.patch.object(Employee_service, "delete_Employee", return_value=expected_response)

    #Act
    response = test_app.delete("/v1/employee/222")

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

    mocker.patch.object(Employee_service, "delete_Employee", return_value=expected_response)

    response = test_app.delete("/v1/employee/3")

    assert response.status_code == 200

def test_search_animal_by_id(test_app, mocker):

    expected_data =  [
            {
            "age": 19,
            "division": "Software Engineer Senior",
            "gender": "male",
            "name": "Kevin",
            "phone": 777
        }
    ]
    
    expected_response = {
        'data': expected_data,
        'status': {
            "code": 200,
            "message": "ini yang kamu cari?"
        }
    }


    mocker.patch.object(Employee_service, 'search_Employee', return_value=expected_response)

    # ACT
    response = test_app.get("/v1/employee/search?name=kevin")

    # ASSERT
    assert response.status_code == 200
    assert response.json['data'] == expected_response


