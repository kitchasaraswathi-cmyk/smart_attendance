from flask import Blueprint, jsonify
from app.services.dashboard_service import get_dashboard_stats
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
    "/notification-logs",
    methods=["GET"]
)
def notification_logs():

    result = fetch_notification_logs()

    return jsonify(result)