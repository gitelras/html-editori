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
        """Tallentaa tiedostopolun tietokantaan.

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
        """Hakee tiedostopolut tietokannasta.

        Returns:
            Tiedostopolut.
        """
        cursor = self._connection.cursor()
        result = cursor.execute(
            "select * from documents"
        )
        files = result.fetchall()
        self._connection.commit()
        return files

    def delete_all(self):
        """Poistaa kaikki polut.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from documents")

        self._connection.commit()

html_repository = Save(get_database_connection())
