from app.models.Employee import Employee
from app.utils.database import db

class Employee_repo():
    def get_list_Employee(self):
        Employees = Employee.query.all()
        return Employees
    
    def update_Employee (self, id, employee):
        employee_obj = Employee.query.get(id)
        employee_obj.name = employee.name
        employee_obj.age = employee.age
        employee_obj.phone = employee.phone
        employee_obj.gender = employee.gender
        employee_obj.division = employee.division

        db.session.commit()
        return employee_obj
    
    def create_Employee(self, employee):
        db.session.add(employee)
        db.session.commit()
        return employee
    

    def search_Employee(self, name):
        employees = Employee.query.filter(Employee.name.like(f"%{name}%")).all()
        return employees
    
    def delete_Employee(self, id):
        employee_obj = Employee.query.get(id)

        db.session.delete(employee_obj)
        db.session.commit()
        return employee_obj