from flask import Blueprint, jsonify, request
from app.services.student_service import (
    fetch_students,
    add_student
)

student_bp = Blueprint('student', __name__)


@student_bp.route('/students', methods=['GET'])
def get_students():

    result = fetch_students()

    return jsonify(result)
@student_bp.route('/students', methods=['POST'])
def create_student():

    data = request.get_json()

    result = add_student(data)

    return jsonify(result)