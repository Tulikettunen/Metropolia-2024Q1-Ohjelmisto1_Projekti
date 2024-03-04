import os
import mysql.connector
from mysql.connector.connection import MySQLConnectionAbstract
from dotenv import load_dotenv
from pathlib import Path


connection: MySQLConnectionAbstract


def create_database_connection():
    """Establishes connection to the database using environment variables."""

    dotenv_path = Path('./config/.env')
    load_dotenv(dotenv_path=dotenv_path)

    global connection
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_DATABASE'),
        port=os.getenv('DB_PORT'),
        username=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        autocommit=bool(os.getenv('DB_AUTOCOMMIT'))
    )

    if connection:
        print("Database connection created.")
