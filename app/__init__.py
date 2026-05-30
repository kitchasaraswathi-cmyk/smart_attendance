import os
from flask import session
from app.routes.student_routes import student_bp

from flask import Flask
from dotenv import load_dotenv
from app.routes.auth_routes import auth_bp
from app.routes.attendance_routes import attendance_bp

from app.database import get_db_connection
from flask_mail import Mail

mail = Mail()

load_dotenv()


def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.config['MYSQL_CONFIG'] = {
        "host": os.getenv('DB_HOST'),
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "database": os.getenv('DB_NAME')
    }
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    

    @app.route('/')
    def home_route():
        return {
            "status": "success",
            "message": "Welcome to Smart Attendance System"
        }

    @app.route('/test')
    def test_route():

        try:
            db_conn = get_db_connection()

            if db_conn and db_conn.is_connected():
                db_conn.close()

                return {
                    "status": "success",
                    "backend": "Alive",
                    "database": "Connected Successfully"
                }

            return {
                "status": "error",
                "database": "Connection Failed"
            }

        except Exception as error:
            return {
                "status": "error",
                "message": str(error)
            }
    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(attendance_bp)
    mail.init_app(app)

    return app