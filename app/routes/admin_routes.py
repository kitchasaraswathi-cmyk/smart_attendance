from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    session,
    redirect
)

from app.services.admin_service import (
    get_admin_stats,
    get_teachers,
    add_teacher,
    update_teacher,
    delete_teacher,
    get_parents,
    add_parent,
    delete_parent,
    get_notifications
)

admin_bp = Blueprint('admin', __name__)




def admin_required():

    if 'user_id' not in session:
        return False

    if session.get('user_role') != 'admin':
        return False

    return True




@admin_bp.route('/admin-dashboard')
def admin_dashboard():

    if not admin_required():
        return redirect('/login')

    return render_template('admin/dashboard.html')


@admin_bp.route('/admin/teachers-page')
def teachers_page():

    if not admin_required():
        return redirect('/login')

    return render_template('admin/teachers.html')


@admin_bp.route('/admin/parents-page')
def parents_page():

    if not admin_required():
        return redirect('/login')

    return render_template('admin/parents.html')


@admin_bp.route('/admin/notifications-page')
def notifications_page():

    if not admin_required():
        return redirect('/login')

    return render_template('admin/notifications.html')


@admin_bp.route('/admin/analytics')
def analytics_page():

    if not admin_required():
        return redirect('/login')

    return render_template('admin/analytics.html')

@admin_bp.route('/admin/students-page')
def students_page():

    if not admin_required():
        return redirect('/login')

    return render_template('admin/students.html')

@admin_bp.route('/admin/attendance-page')
def attendance_page():

    if not admin_required():
        return redirect('/login')

    return render_template(
        'admin/attendance.html'
    )




@admin_bp.route('/admin/stats', methods=['GET'])
def admin_stats():

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify(get_admin_stats())




@admin_bp.route('/admin/teachers', methods=['GET'])
def teachers_list():

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify(get_teachers())


@admin_bp.route('/admin/teachers', methods=['POST'])
def create_teacher():

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    data = request.get_json()

    return jsonify(add_teacher(data))


@admin_bp.route('/admin/teachers/<int:id>', methods=['PUT'])
def edit_teacher(id):

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    data = request.get_json()

    return jsonify(update_teacher(id, data))


@admin_bp.route('/admin/teachers/<int:id>', methods=['DELETE'])
def remove_teacher(id):

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify(delete_teacher(id))




@admin_bp.route('/admin/parents', methods=['GET'])
def parents_list():

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify(get_parents())


@admin_bp.route('/admin/parents', methods=['POST'])
def create_parent():

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    data = request.get_json()

    return jsonify(add_parent(data))


@admin_bp.route('/admin/parents/<int:id>', methods=['DELETE'])
def remove_parent(id):

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify(delete_parent(id))




@admin_bp.route('/admin/notifications', methods=['GET'])
def notifications():

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify(get_notifications())



@admin_bp.route('/admin/me', methods=['GET'])
def admin_me():

    if not admin_required():
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 401

    return jsonify({
        "status": "success",
        "user_id": session.get('user_id'),
        "role": session.get('user_role')
    })