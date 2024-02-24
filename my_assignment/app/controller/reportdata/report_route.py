from app.utils.database import db
from flask import Blueprint, jsonify, request
# from pydantic import ValidationError
from app.controller.reportdata.Schema.create_report_req import Create_animal_report_request
from app.models.report_model.reports import Animal_report
from app.utils.api_response import api_response
from app.services.report_service.ar_service import Ar_Services
from app.controller.reportdata.Schema.update_report_req import Update_animal_report_request

report_blueprint = Blueprint('report_endpoint', __name__)

@report_blueprint.route('/animals', methods=["GET"])

def get_animal_report():

    try:

        report_service = Ar_Services()

        animal_report = report_service.get_animal_reports()
        return api_response(
            status_code=200,
            message="Animal-zoo-Report",
            data=animal_report
        )
    except Exception as e:
        return "failed to fetch all data", 500  
    
@report_blueprint.route('/animals/<int:report_id>', methods=["GET"])
def get_animal_reports(report_id):
    try:
        ar = Animal_report.query.get(report_id)
        if not ar:
            return api_response(
                status_code=404,
                message="animal report's not found",
                data=None
            )
        return api_response(
            status_code=200,
            message="",
            data=ar.as_dict()
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=None
        )
    
@report_blueprint.route('/animals/search', methods=["GET"])
def search_animal_report():
    try:
        request_data = request.args
        report_service = Ar_Services()
        ar = report_service.search_animal_report(request_data["name"])
        return api_response(
            status_code=200,
            message="",
            data=ar
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=None
        )
    
@report_blueprint.route('/animals', methods=["POST"])
def create_animal_report_endpoint():
    try:
        data = request.json
        ar = Animal_report(
            report_number=data['report_number'],
            report_date=data['report_date'],
            name=data['name'],
            role=data['role'],
            explanation=data['explanation']
        )

        db.session.add(ar)
        db.session.commit()
        return "added successfully", 200
    except Exception as e:
        return str(e), 200
    
@report_blueprint.route('/animals/<int:report_id>', methods=["PUT"])
def update_animal_report(report_id):
    try:
        data = request.json
        update_ar_request = Update_animal_report_request(**data)
        ar_service = Ar_Services()
        ar = ar_service.update_animal_report(report_id, update_ar_request)
        return api_response(
            status_code=200,
            message="The Reports are updated successfully",
            data=ar
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=None
        )

    

# @report_blueprint.route('/visitors', methods=["GET"])

# def get_visitor_report():

#     try:

#         report_service = Report_Services()

#         visitor_report = report_service.get_visitor_reports()
#         return api_response(
#             status_code=200,
#             message="Visitor's-Reports",
#             data=visitor_report
#         )
#     except Exception as e:
#         return "failed to fetch all data", 500  


# @report_blueprint.route('/revenue', methods=["GET"])

# def get_visitor_report():
#     try:

#         report_service = Report_Services()

#         revenue_report = report_service.get_revenue_reports()
#         return api_response(
#             status_code=200,
#             message="Revenue-Reports",
#             data=revenue_report
#         )
#     except Exception as e:
#         return "failed to fetch all data", 500  
    
