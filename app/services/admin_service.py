from app.database import get_db_connection
from werkzeug.security import generate_password_hash



def get_admin_stats():

    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT COUNT(*) AS total_students FROM students")
        students = cursor.fetchone()['total_students']

        cursor.execute(
            "SELECT COUNT(*) AS total_teachers FROM users WHERE role='teacher'"
        )
        teachers = cursor.fetchone()['total_teachers']

        cursor.execute(
            "SELECT COUNT(*) AS total_parents FROM users WHERE role='parent'"
        )
        parents = cursor.fetchone()['total_parents']

        cursor.execute(
            "SELECT COUNT(*) AS total_notifications FROM notification_logs"
        )
        notifications = cursor.fetchone()['total_notifications']

        return {
            "status": "success",
            "stats": {
                "students": students,
                "teachers": teachers,
                "parents": parents,
                "notifications": notifications
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        cursor.close()
        db.close()




def get_teachers():

    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT
            id,
            full_name,
            email,
            role,
            created_at
            FROM users
            WHERE role='teacher'
            ORDER BY id DESC
        """)

        teachers = cursor.fetchall()

        return {
            "status": "success",
            "teachers": teachers
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        cursor.close()
        db.close()


def add_teacher(data):

    try:

        db = get_db_connection()
        cursor = db.cursor()

        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')

        password_hash = generate_password_hash(password)

        cursor.execute("""
            INSERT INTO users
            (
                full_name,
                email,
                password_hash,
                role
            )
            VALUES
            (%s,%s,%s,'teacher')
        """,
        (
            full_name,
            email,
            password_hash
        ))

        db.commit()

        return {
            "status": "success",
            "message": "Teacher added successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        cursor.close()
        db.close()


def update_teacher(id,data):

    try:

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("""
            UPDATE users
            SET
            full_name=%s,
            email=%s
            WHERE id=%s
            AND role='teacher'
        """,
        (
            data.get('full_name'),
            data.get('email'),
            id
        ))

        db.commit()

        return {
            "status":"success",
            "message":"Teacher updated successfully"
        }

    except Exception as e:

        return {
            "status":"error",
            "message":str(e)
        }

    finally:

        cursor.close()
        db.close()


def delete_teacher(id):

    try:

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("""
            DELETE FROM users
            WHERE id=%s
            AND role='teacher'
        """,(id,))

        db.commit()

        return {
            "status":"success",
            "message":"Teacher deleted successfully"
        }

    except Exception as e:

        return {
            "status":"error",
            "message":str(e)
        }

    finally:

        cursor.close()
        db.close()




def get_parents():

    try:

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT
            id,
            full_name,
            email,
            role,
            created_at
            FROM users
            WHERE role='parent'
            ORDER BY id DESC
        """)

        parents = cursor.fetchall()

        return {
            "status":"success",
            "parents":parents
        }

    except Exception as e:

        return {
            "status":"error",
            "message":str(e)
        }

    finally:

        cursor.close()
        db.close()


def add_parent(data):

    try:

        db = get_db_connection()
        cursor = db.cursor()

        password_hash = generate_password_hash(
            data.get('password')
        )

        cursor.execute("""
            INSERT INTO users
            (
                full_name,
                email,
                password_hash,
                role
            )
            VALUES
            (%s,%s,%s,'parent')
        """,
        (
            data.get('full_name'),
            data.get('email'),
            password_hash
        ))

        db.commit()

        return {
            "status":"success",
            "message":"Parent added successfully"
        }

    except Exception as e:

        return {
            "status":"error",
            "message":str(e)
        }

    finally:

        cursor.close()
        db.close()


def delete_parent(id):

    try:

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("""
            DELETE FROM users
            WHERE id=%s
            AND role='parent'
        """,(id,))

        db.commit()

        return {
            "status":"success",
            "message":"Parent deleted successfully"
        }

    except Exception as e:

        return {
            "status":"error",
            "message":str(e)
        }

    finally:

        cursor.close()
        db.close()



def get_notifications():

    try:

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM notification_logs
            ORDER BY id DESC
        """)

        logs = cursor.fetchall()

        return {
            "status":"success",
            "notifications":logs
        }

    except Exception as e:

        return {
            "status":"error",
            "message":str(e)
        }

    finally:

        cursor.close()
        db.close()