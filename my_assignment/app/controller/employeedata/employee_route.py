from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from app.controller.employeedata.Schema.create_employee_req import Create_employee_request
from ...utils.database import db
from app.models.Employee import Employee
from app.utils.api_response import api_response
from app.services.employee_services import Employee_service
from app.controller.employeedata.Schema.update_employee_req import Update_employee_request

employee_blueprint = Blueprint('employee_endpoint', __name__)

@employee_blueprint.route('/', methods=["GET"])
def get_list_Employee():

    try:

        employee_service = Employee_service()

        employees = employee_service.get_Employees()
        return api_response(
            status_code=200,
            message="",
            data=employees
        )
    except Exception as e:
        return "failed to fetch all data", 500
    
@employee_blueprint.route('/<int:employee_id>', methods=["GET"])
def get_Employee(employee_id):
        
    try:
        employee = Employee.query.get(employee_id)

        if not employee:
            return "employee not found", 404
        
        return employee.as_dict(), 200
    except Exception as e:
        return str(e), 500
    
@employee_blueprint.route('/search', methods=["GET"])
def search_Employee():
        
    try:

        request_data = request.args

        employee_service = Employee_service()

        employees = employee_service.search_Employee(request_data["name"])
        return api_response(
            status_code=200,
            message="",
            data=employees
        )
    except Exception as e:
        return str(e), 500
    

@employee_blueprint.route('/', methods=["POST"])
def create_Employee():

    try:
        data = request.json
        update_employee_request = Create_employee_request(**data)

        employee_service = Employee_service()

        employees = employee_service.create_employee(update_employee_request)

        return api_response(
            status_code=201,
            message="berhasil ditambahkan",
            data= employees
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
    
@employee_blueprint.route('/<int:employee_id>', methods=["PUT"])
def update_Employee(employee_id):

    try:
        
        data = request.json
        update_employee_request = Update_employee_request(**data)

        employee_service = Employee_service()
        employees = employee_service.update_Employee(employee_id,update_employee_request)
        
        return api_response(
            status_code=200,
            message="update berhasil",
            data=employees
        )
    except Exception as e:
        return str(e), 500
    
@employee_blueprint.route('/<int:employee_id>', methods=["DELETE"])

def delete_Employee(employee_id):
    try:
        employee_service = Employee_service()
        is_deleted = employee_service.delete_Employee(employee_id)
        
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