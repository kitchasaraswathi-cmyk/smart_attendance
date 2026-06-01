from flask import Blueprint, jsonify, render_template

# 1. FIXED: Imported your missing service layout functions explicitly
from app.services.dashboard_service import (
    get_dashboard_stats,
    get_notification_count
)
from app.services.email_service import fetch_notification_logs
from app.services.student_service import fetch_students, add_student  # Added these
from app.services.attendance_service import fetch_attendance, mark_attendance, fetch_absentees  # Added these

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


# =====================================================================
#  HTML TEMPLATE VIEW ROUTES (Renders the actual browser layout pages)
# =====================================================================

@dashboard_bp.route('/teacher-dashboard', methods=["GET"])
def teacher_dashboard():
    return render_template('teacher/dashboard.html')

@dashboard_bp.route('/teacher/students', methods=["GET"])
def teacher_students_page():
    # FIXED: Added the missing route for your students control panel file
    return render_template('teacher/students.html')

@dashboard_bp.route('/teacher/attendance', methods=["GET"])
def teacher_attendance_page():
    # FIXED: Added the missing route for your active roll call sheet file
    return render_template('teacher/attendance.html')

@dashboard_bp.route('/teacher/reports', methods=["GET"])
def teacher_reports_page():
    # FIXED: Added the missing route for your parent notification outbox log file
    return render_template('teacher/reports.html')



# =====================================================================
#  JSON TELEMETRY API ENDPOINTS (Feeds data dynamically to your JavaScript fetch)
# =====================================================================

@dashboard_bp.route("/dashboard-stats", methods=["GET"])
def dashboard_stats():
    result = get_dashboard_stats()
    return jsonify(result)

@dashboard_bp.route("/notification-count", methods=["GET"])
def notification_count():
    result = get_notification_count()
    return jsonify(result)

@dashboard_bp.route("/notification-logs", methods=["GET"])
def notification_logs():
    result = fetch_notification_logs()
    return jsonify(result)

@dashboard_bp.route("/absentees", methods=["GET"])
def absentees_log():
    # FIXED: Added missing data stream to populate the home dashboard chart/table cards
    result = fetch_absentees()
    return jsonify(result)

@dashboard_bp.route("/api/students", methods=["GET"])
def get_students():
    # FIXED: Swapped out the unimported "fetch_all_students()" with your actual service function
    result = fetch_students() 
    return jsonify(result)

@dashboard_bp.route("/students", methods=["POST"])
def post_new_student():
    # FIXED: Added the POST handler requested by the "Enroll New Student" frontend form modal
    from flask import request
    data = request.get_json()
    result = add_student(data)
    return jsonify(result)

@dashboard_bp.route("/attendance", methods=["GET", "POST"])
def handle_attendance():
    # FIXED: Provides dual compatibility to record daily marks or pull global history arrays
    from flask import request
    if request.method == "POST":
        data = request.get_json()
        result = mark_attendance(data)
        return jsonify(result)
    else:
        result = fetch_attendance()
        return jsonify(result)