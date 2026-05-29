from app.database import get_db_connection


def mark_attendance(data):

    student_id = data.get('student_id')
    attendance_date = data.get('attendance_date')
    status = data.get('status')

    # Validation
    if not student_id or not attendance_date or not status:

        return {
            "status": "error",
            "message": "All fields are required"
        }

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor()

        query = """
            INSERT INTO attendance
            (
                student_id,
                attendance_date,
                status
            )
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (
                student_id,
                attendance_date,
                status
            )
        )

        db_conn.commit()

        return {
            "status": "success",
            "message": "Attendance marked successfully"
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()
def fetch_attendance():

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor(dictionary=True)

        query = """
            SELECT
                attendance.id,
                students.full_name,
                students.roll_number,
                attendance.attendance_date,
                attendance.status
            FROM attendance
            JOIN students
            ON attendance.student_id = students.id
            ORDER BY attendance.attendance_date DESC
        """

        cursor.execute(query)

        records = cursor.fetchall()

        return {
            "status": "success",
            "attendance": records
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()
def fetch_absentees():

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor(dictionary=True)

        query = """
            SELECT
                students.full_name,
                students.roll_number,
                students.class_name,
                students.parent_email,
                students.parent_phone,
                attendance.attendance_date
            FROM attendance
            JOIN students
            ON attendance.student_id = students.id
            WHERE attendance.status = 'absent'
            ORDER BY attendance.attendance_date DESC
        """

        cursor.execute(query)

        absentees = cursor.fetchall()

        return {
            "status": "success",
            "absentees": absentees
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()