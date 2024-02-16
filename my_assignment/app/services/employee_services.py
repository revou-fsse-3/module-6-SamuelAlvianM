from app.repositories.employee_repo import Employee_repo
from app.utils.database import db


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

    def update_Employee (self, id, employee_data_dto):
        updated_employee = self.employee_repo.update_Employee(id, employee_data_dto)
        return updated_employee.as_dict()
    
    def delete_Employee(self, id):
        is_deleted = self.employee_repo.delete_Employee(id)
        return is_deleted