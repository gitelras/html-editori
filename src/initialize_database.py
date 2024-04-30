from database_connection import get_database_connection

def drop_tables(connection):
    #cursor = connection.cursor()
    #cursor.execute('''
    #    drop table if exists ;
    #''')
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table documents (
            ID PRIMERY KEY,
            path TEXT
        );
    ''')

    connection.commit()

def initialize_database():
    """Alustaa tietokantataulut."""

    connection = get_database_connection()

    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
