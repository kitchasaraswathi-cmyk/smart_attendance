from flask import Blueprint, jsonify
from app.services.student_service import fetch_students

student_bp = Blueprint('student', __name__)


@student_bp.route('/students', methods=['GET'])
def get_students():

    result = fetch_students()

    return jsonify(result)