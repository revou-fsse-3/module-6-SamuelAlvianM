from flask import Flask
from app.controller.employeedata import employee_route
from app.controller.animaldata import animal_route
from app.controller.feedingdata import feeding_route
from app.controller.reportdata import report_route
import os
from app.utils.database import db


app = Flask(__name__)   

DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(animal_route.animal_blueprint, url_prefix="/v1/animals")
app.register_blueprint(employee_route.employee_blueprint, url_prefix="/v1/employee")
app.register_blueprint(feeding_route.feeding_blueprint, url_prefix="/v1/animals/feeding-time")
app.register_blueprint(report_route.report_blueprint, url_prefix="/v1/reports")
