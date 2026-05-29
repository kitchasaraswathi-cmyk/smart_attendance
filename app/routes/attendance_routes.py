from flask import Blueprint, jsonify

attendance_bp = Blueprint('attendance', __name__)


@attendance_bp.route('/attendance', methods=['GET'])
def attendance_home():

    return jsonify({
        "status": "success",
        "message": "Attendance route working"
    })