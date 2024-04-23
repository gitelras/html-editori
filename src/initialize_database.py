#from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists Calculations;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table HTML (
            ID PRIMERY KEY,
            div TEXT
        );
    ''')

    connection.commit()
