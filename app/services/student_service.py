from app.database import get_db_connection


def fetch_students():

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor(dictionary=True)

        query = "SELECT * FROM students"

        cursor.execute(query)

        students = cursor.fetchall()

        return {
            "status": "success",
            "students": students
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()
def add_student(data):

    full_name = data.get('full_name')
    roll_number = data.get('roll_number')
    class_name = data.get('class_name')
    parent_email = data.get('parent_email')
    parent_phone = data.get('parent_phone')

    # Validation
    if not full_name or not roll_number or not class_name:

        return {
            "status": "error",
            "message": "Required fields missing"
        }

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor()

        query = """
            INSERT INTO students
            (
                full_name,
                roll_number,
                class_name,
                parent_email,
                parent_phone
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                full_name,
                roll_number,
                class_name,
                parent_email,
                parent_phone
            )
        )

        db_conn.commit()

        return {
            "status": "success",
            "message": "Student added successfully"
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()