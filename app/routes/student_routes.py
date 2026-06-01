from flask import Blueprint, jsonify, request
from flask import Blueprint, jsonify, request

from app.services.student_service import (
    fetch_students,
    add_student,
    fetch_student_by_id,
    update_student,
    delete_student
)

student_bp = Blueprint(
    "student",
    __name__
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

@student_bp.route(
    "/students/<int:student_id>",
    methods=["GET"]
)
def get_student(student_id):

    result = fetch_student_by_id(student_id)

    return jsonify(result)





@student_bp.route(
    "/students/<int:student_id>",
    methods=["PUT"]
)
def edit_student(student_id):

    data = request.get_json()

    result = update_student(
        student_id,
        data
    )

    return jsonify(result)

@student_bp.route(
    "/students/<int:student_id>",
    methods=["DELETE"]
)
def remove_student(student_id):

    result = delete_student(student_id)

    return jsonify(result)