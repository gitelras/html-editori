from database_connection import get_database_connection

class Save:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
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
            todo: Tallennettava käyttäjä User-oliona.

        Returns:
            Tallennettu käyttjä User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into documents (path) values (?)",
            (path,)
        )

        self._connection.commit()

        return path


html_repository = Save(get_database_connection())
