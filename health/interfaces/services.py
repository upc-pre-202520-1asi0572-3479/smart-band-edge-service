from flask import Blueprint, request, jsonify

from health.application.services import HealthRecordApplicationService
from iam.interfaces.services import authenticate_request

health_api = Blueprint('health_api', __name__)

# Initialize dependencies
health_record_service = HealthRecordApplicationService()

@health_api.route("/api/v1/health-monitoring/data-records", methods=["POST"])
def create_health_record():
    """
    Endpoint to create a new health record.
    Expects JSON body with 'device_id', 'bpm', and optional 'created_at'.
    Requires 'X-API-Key' header for authentication.

    :return:
    JSON response with the created health record or error message.
    201 Created on success, 400 Bad Request on failure, 401 Unauthorized if authentication
    """
    auth_result = authenticate_request()
    if auth_result:
        return auth_result  # Return authentication error if any
    data = request.json
    try:
        device_id = data["device_id"]
        bpm = data["bpm"]
        created_at = data.get("created_at")
        record = health_record_service.create_health_record(device_id, bpm, created_at, request.headers.get("X-API-Key"))
        return jsonify({
            "id": record.id,
            "device_id": record.device_id,
            "bpm": record.bpm,
            "created_at": record.created_at.isoformat() + "Z"
        }), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
