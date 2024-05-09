# conftest.py
import os
from dotenv import load_dotenv

def pytest_configure():
    # Määrittele testiympäristön .env-tiedosto suhteellinen polku
    # Huomaa, että '..' nousee yhden tason ylös hakemistorakenteessa,
    # joten tarvitsemme kaksi '..' päästäksemme 'Ohjelmistotekniikka' hakemistoon.
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env.test')
    load_dotenv(dotenv_path=dotenv_path, override=True)

    # Kutsu tietokannan alustustoimintoa
    from build import build
    build()
