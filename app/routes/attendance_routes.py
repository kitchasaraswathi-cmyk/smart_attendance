from flask import Blueprint, jsonify, request
from app.services.attendance_service import (
    mark_attendance,
    fetch_attendance, fetch_absentees
)

attendance_bp = Blueprint('attendance', __name__)


@attendance_bp.route('/attendance', methods=['GET'])
def get_attendance():

    result = fetch_attendance()

    return jsonify(result)
@attendance_bp.route('/attendance', methods=['POST'])
def create_attendance():

    data = request.get_json()

    result = mark_attendance(data)

    return jsonify(result)
@attendance_bp.route('/absentees', methods=['GET'])
def get_absentees():

    result = fetch_absentees()

    return jsonify(result)