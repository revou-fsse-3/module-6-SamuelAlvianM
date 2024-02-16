from flask import Blueprint, jsonify, request
from ...utils.database import db
from app.models.feeding import Feeding
from app.utils.api_response import api_response
from app.services.feeding_services import Feeding_service
from app.controller.feedingdata.Schema.update_feeding_req import Update_feeding_request

feeding_blueprint = Blueprint('feeding_endpoint', __name__)

@feeding_blueprint.route('/', methods=["GET"])
def get_list_feeding():
    try:
        feeding_service = Feeding_service()
        feeds = feeding_service.get_feeding()
        return api_response(
            status_code=200,
            message="",
            data=feeds
        )
    except Exception as e:
        return "failed to fetch all data", 500
    
    
@feeding_blueprint.route('/<int:feeding_id>', methods=["GET"])
def get_feeding(feeding_id):
    try:
        feeds = Feeding.query.get(feeding_id)
        if not feeds:
            return api_response(
                status_code=404,
                message="Feeding schedule not found",
                data=None
            )
        return api_response(
            status_code=200,
            message="",
            data=feeds.as_dict()
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=None
        )

@feeding_blueprint.route('/search', methods=["GET"])
def search_feeding():
    try:
        request_data = request.args
        feeding_service = Feeding_service()
        feeds = feeding_service.search_feeding(request_data["name"])
        return api_response(
            status_code=200,
            message="",
            data=feeds
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=None
        )

@feeding_blueprint.route('/', methods=["POST"])
def create_feeding():
    try:
        data = request.json
        feeds = Feeding()
        feeds.name=data['name'],
        feeds.feeding_time=data['feeding_time'],
        feeds.food_count_kg=data['food_count_kg'],
        feeds.food_type=data['food_type'],

        db.session.add(feeds)
        db.session.commit()
        return "added successfully", 200
    except Exception as e:
        return e, 200

@feeding_blueprint.route('/<int:feeding_id>', methods=["PUT"])
def update_feeding(feeding_id):
    try:
        data = request.json
        update_feeding_request = Update_feeding_request(**data)
        feeding_service = Feeding_service()
        feeds = feeding_service.update_feeding(feeding_id, update_feeding_request)
        return api_response(
            status_code=200,
            message="Feeding schedule updated successfully",
            data=feeds
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=None
        )

@feeding_blueprint.route('/<int:feeding_id>', methods=["DELETE"])
def delete_feeding(feeding_id):
    try:
        feeding_service = Feeding_service()
        is_deleted = feeding_service.delete_feeding(feeding_id)
        if is_deleted:
            return api_response(
                status_code=200,
                message="Feeding schedule deleted successfully",
                data=None
            )
        else:
            return api_response(
                status_code=404,
                message="Feeding schedule not found",
                data=None
            )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=None
        )
