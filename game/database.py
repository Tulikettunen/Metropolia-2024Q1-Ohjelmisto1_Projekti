import os
import mysql.connector
from mysql.connector.connection import MySQLConnectionAbstract
from mysql.connector import Error as DB_error
from dotenv import load_dotenv
from pathlib import Path


connection: MySQLConnectionAbstract


def create_database_connection() -> DB_error or None:
    """
    Establishes connection to the database using environment variables.

    :returns: Error in case of an error and None if no error occur.
    """

    dotenv_path = Path('./config/.env')
    load_dotenv(dotenv_path=dotenv_path)

    try:
        global connection
        connection = mysql.connector.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            port=os.getenv('PORT'),
            username=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            autocommit=bool(os.getenv('AUTOCOMMIT'))
        )

        return None
    except DB_error as error:
        return error
