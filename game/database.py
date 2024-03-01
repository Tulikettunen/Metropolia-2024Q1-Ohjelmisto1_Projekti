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
    :raises mysql.connector.Error: If the database connection creation fails
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


def fetch_10_random_airports_from_db() -> list or DB_error:
    """
    Fetches 10 random airports from database.

    :returns: List of airports as tuples
    :rtype: [(string, string, float, float)]
    :raises mysql.connector.Error: If the database fetch fails
    """

    sql = ("SELECT airport.name, country.name, airport.latitude_deg, airport.longitude_deg "
           "FROM airport, country WHERE airport.iso_country = country.iso_country AND NOT airport.ident = 'EFHK' "
           "ORDER BY RAND() LIMIT 10")
    # The 'AND NOT airport.ident' is used to strip 'Helsinki Vantaa Airport'
    # out of the query, because it is the start airport

    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    except DB_error as error:
        return error


def fetch_10_random_parcels_from_db() -> list or DB_error:
    """
    Fetches 10 random parcels from database.

    :returns: List of parcels as tuple
    :rtype: [(string, int, int, string)]
    :raises mysql.connector.Error: If the database fetch fails
    """

    sql = "SELECT item, item_co2, item_type, item_info FROM parcel ORDER BY RAND() LIMIT 10"

    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    except DB_error as error:
        return error
