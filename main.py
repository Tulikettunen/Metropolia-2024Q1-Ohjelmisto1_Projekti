import game.database as database
import game.logic as game


def main():
    database.create_database_connection()
    game.start()


if __name__ == "__main__":
    main()

