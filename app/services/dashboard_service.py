from app.database import get_db_connection
from datetime import date


def get_dashboard_stats():

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor(dictionary=True)

        today = date.today()

        # Total Students
        cursor.execute(
            "SELECT COUNT(*) AS total_students FROM students"
        )
        total_students = cursor.fetchone()["total_students"]

        # Present Today
        cursor.execute(
            """
            SELECT COUNT(*) AS present_today
            FROM attendance
            WHERE attendance_date = %s
            AND status = 'present'
            """,
            (today,)
        )
        present_today = cursor.fetchone()["present_today"]

        # Absent Today
        cursor.execute(
            """
            SELECT COUNT(*) AS absent_today
            FROM attendance
            WHERE attendance_date = %s
            AND status = 'absent'
            """,
            (today,)
        )
        absent_today = cursor.fetchone()["absent_today"]

        # Emails Sent Today
        cursor.execute(
            """
            SELECT COUNT(*) AS emails_sent_today
            FROM notification_logs
            WHERE DATE(sent_at) = %s
            """,
            (today,)
        )
        emails_sent_today = cursor.fetchone()["emails_sent_today"]

        return {
            "status": "success",
            "total_students": total_students,
            "present_today": present_today,
            "absent_today": absent_today,
            "emails_sent_today": emails_sent_today
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()