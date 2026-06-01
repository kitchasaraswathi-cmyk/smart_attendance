from flask import Blueprint, jsonify, render_template
from app.services.dashboard_service import (
    get_dashboard_stats,
    get_notification_count
)
from app.services.email_service import fetch_notification_logs

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route(
    "/dashboard-stats",
    methods=["GET"]
)
def dashboard():

    result = get_dashboard_stats()

    return jsonify(result)

@dashboard_bp.route(
    "/notification-count",
    methods=["GET"]
)
def notification_count():

    result = get_notification_count()

    return jsonify(result)

@dashboard_bp.route(
    "/notification-logs",
    methods=["GET"]
)
def notification_logs():

    result = fetch_notification_logs()

    return jsonify(result)

@dashboard_bp.route('/teacher-dashboard')
def teacher_dashboard():
    return render_template(
        'teacher/dashboard.html'
    )

@dashboard_bp.route(
    "/api/students",
    methods=["GET"]
)
def get_students():

    students =fetch_all_students()

    return jsonify({
        "students": students
    })