from flask_mail import Message
from app.extensions import mail
from app.database import get_db_connection


def send_test_email(recipient_email):

    try:

        msg = Message(
            subject="Smart Attendance System Test",
            recipients=[recipient_email]
        )

        msg.body = """
Hello,

This is a test email from Smart Attendance System.

If you received this email, Flask-Mail is working successfully.

Regards,
Smart Attendance System
"""

        mail.send(msg)

        return {
            "status": "success",
            "message": f"Email sent to {recipient_email}"
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }
def send_absentee_notification(
    student_id,
    parent_email,
    student_name,
    attendance_date
):

    try:

        msg = Message(
            subject="Attendance Alert",
            recipients=[parent_email]
        )

        msg.body = f"""
Dear Parent,

This is to inform you that your child {student_name}
was marked absent on {attendance_date}.

Please contact the school if you need further information.

Regards,
Smart Attendance System
"""

        mail.send(msg)

        save_notification_log(
            student_id,
            parent_email,
            "EMAIL"
        )

        return True

    except Exception as error:

        print("Email Error:", error)
        return False
def save_notification_log(
    student_id,
    parent_email,
    notification_type="EMAIL"
):

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor()

        query = """
            INSERT INTO notification_logs
            (
                student_id,
                parent_email,
                notification_type
            )
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (
                student_id,
                parent_email,
                notification_type
            )
        )

        db_conn.commit()

    except Exception as error:

        print("Notification Log Error:", error)

    finally:

        cursor.close()
        db_conn.close()

def fetch_notification_logs():

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor(dictionary=True)

        query = """
            SELECT
                id,
                student_id,
                parent_email,
                notification_type,
                sent_at
            FROM notification_logs
            ORDER BY sent_at DESC
        """

        cursor.execute(query)

        logs = cursor.fetchall()

        return {
            "status": "success",
            "logs": logs
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()