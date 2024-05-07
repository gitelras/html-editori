from database_connection import get_database_connection

class Save:
    """Html-tiedostopolkujen tallentamiseen liittyvistä
        tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def create(self, path):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            path: Tallennettava tiedostopolku.

        Returns:
            Tallennettu tiedostopolku.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into documents (path) values (?)",
            (path,)
        )

        self._connection.commit()

        return path
    
    def get_files(self):
        cursor = self._connection.cursor()
        result = cursor.execute(
            "select * from documents"
        )
        files = result.fetchall()

        for i in files:
            print(i)

        self._connection.commit()

        return files



html_repository = Save(get_database_connection())
