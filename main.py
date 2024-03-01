import game.database as database


def main():
    err = database.create_database_connection()
    if err:
        print(f"Error occurred while creating new database connection: {err}")
    else:
        print("Database connection established.")
        # start the app


if __name__ == "__main__":
    main()
