from app.repositories.employee_repo import Employee_repo
from app.utils.database import db
from app.models.Employee import Employee


class Employee_service:

    def __init__(self):
        self.employee_repo = Employee_repo()

    def get_Employees(self):
        employees = self.employee_repo.get_list_Employee()
        print(employees)
        return [employee.as_dict() for employee in employees]
    
    def search_Employee(self, name):
        employees = self.employee_repo.search_Employee(name)
        return [employee.as_dict() for employee in employees]
    
    def create_employee(self, employee_data_dto):
        employee = Employee()

        employee.name = employee_data_dto.name
        employee.age = employee_data_dto.age
        employee.phone = employee_data_dto.phone        
        employee.gender = employee_data_dto.gender
        employee.division = employee_data_dto.division
        return employee.as_dict()

    def update_Employee (self, id, employee_data_dto):
        updated_employee = self.employee_repo.update_Employee(id, employee_data_dto)
        return updated_employee.as_dict()
    
    def delete_Employee(self, id):
        employee = Employee.query.get(id)
        if not employee:
            return "Data tidak ditemukan"

        is_deleted = self.employee_repo.delete_employee(id)
        return is_deleted.as_dict()