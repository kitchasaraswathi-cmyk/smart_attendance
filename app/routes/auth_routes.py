from flask import Blueprint, request, jsonify, session

from app.services.auth_service import register_user, login_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    result = register_user(data)

    return jsonify(result)
@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    result = login_user(data)

# Create session after successful login
    if result['status'] == 'success':

       session['user_id'] = result['user']['id']

       session['user_role'] = result['user']['role']

    return jsonify(result) 
@auth_bp.route('/dashboard', methods=['GET'])
def dashboard():

    # Check session
    if 'user_id' not in session:

        return jsonify({
            "status": "error",
            "message": "Unauthorized access"
        })

    return jsonify({
        "status": "success",
        "message": "Welcome to Dashboard",
        "user_id": session['user_id'],
        "role": session['user_role']
    })