
from app.controller.employeedata.Schema.create_employee_req import Create_employee_request
from app.models.Employee import Employee
from app.services.employee_services import Employee_service
from app.repositories.employee_repo import Employee_repo

def test_get_list_employee_success(mocker):

    #Arrange
    mock_employee_data = [
        Employee(
            id=2, 
            name="dewa", 
            age=17, 
            gender="man",
            phone=777,
            division="co-d"
        ),
        Employee(
            id=4, 
            name="jean", 
            age=17, 
            gender="male",
            phone=777,
            division="manager"
        ),
    ]
    mocker.patch.object(Employee_repo, 'get_list_Employee', return_value=mock_employee_data)

    #Act
    employee_service = Employee_service().get_Employees()

    #Assert
    assert len(employee_service) == 2
    assert employee_service[0]['name'] == 'dewa'
    assert employee_service[1]['division'] == 'manager'


def test_create_employee_success(test_app, mocker):

    mock_employee_data = Employee(
            id=2, 
            name="dewa", 
            age=17, 
            gender="man",
            phone=777,
            division="co-d"
        ),
    mocker.patch.object(Employee_repo, 'create_Employee', return_value=mock_employee_data)

    create_dto = Create_employee_request(
            name="dewa", 
            age=17, 
            gender="man",
            phone=777,
            division="co-d"
    )


    employee_service_create = test_app.post("/v1/employee/", json=Employee_service().create_employee(create_dto))
    
    assert employee_service_create.json['data']['name'] == "dewa"
    assert employee_service_create.status_code == 201


