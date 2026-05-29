import mysql.connector

from flask import current_app


def get_db_connection():

    try:

        db_config = current_app.config['MYSQL_CONFIG']

        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )

        return connection

    except mysql.connector.Error as error:

        print(error)

        return None