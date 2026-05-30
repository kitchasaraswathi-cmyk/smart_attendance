from flask_mail import Message
from app.extensions import mail


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

        return True

    except Exception as error:

        print("Email Error:", error)
        return False