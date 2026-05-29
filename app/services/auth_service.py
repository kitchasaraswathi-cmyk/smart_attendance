from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.database import get_db_connection


def register_user(data):

    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')

    # Check empty fields
    if not full_name or not email or not password:

        return {
            "status": "error",
            "message": "All fields are required"
        }

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor(dictionary=True)

        # Check existing email
        check_query = "SELECT * FROM users WHERE email = %s"

        cursor.execute(check_query, (email,))

        existing_user = cursor.fetchone()

        if existing_user:

            return {
                "status": "error",
                "message": "Email already exists"
            }

        # Hash password
        hashed_password = generate_password_hash(password)

        # Insert user
        insert_query = """
            INSERT INTO users
            (full_name, email, password_hash)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            insert_query,
            (full_name, email, hashed_password)
        )

        db_conn.commit()

        return {
            "status": "success",
            "message": "User registered successfully"
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()
def login_user(data):

    email = data.get('email')
    password = data.get('password')

    # Check empty fields
    if not email or not password:

        return {
            "status": "error",
            "message": "Email and password are required"
        }

    try:

        db_conn = get_db_connection()

        cursor = db_conn.cursor(dictionary=True)

        # Find user by email
        query = "SELECT * FROM users WHERE email = %s"

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        # User not found
        if not user:

            return {
                "status": "error",
                "message": "Invalid email"
            }

        # Verify password
        password_valid = check_password_hash(
            user['password_hash'],
            password
        )

        if not password_valid:

            return {
                "status": "error",
                "message": "Invalid password"
            }

        return {
           "status": "success",
           "message": "Login successful",
           "user": {
           "id": user['id'],
           "full_name": user['full_name'],
           "email": user['email'],
           "role": user['role']
           }
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }

    finally:

        cursor.close()
        db_conn.close()