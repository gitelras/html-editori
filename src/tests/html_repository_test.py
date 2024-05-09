import unittest
import os
from repositories.html_repository import Save
from services.html_builder import HtmlBuilder
from database_connection import get_database_connection

class TestHtmlRepository(unittest.TestCase):
    def setUp(self):
        #os.environ['DATABASE_FILENAME'] = 'test-database.sqlite'
        self.save = Save(get_database_connection())
        self.save.delete_all()
        self.html_builder = HtmlBuilder()
        self.html_builder.create_html_file("path", "name")
    
    def test_database(self):
        files = self.save.get_files()
        self.assertEqual(len(files), 1)

    def tearDown(self):
        self.save.delete_all()
        files = self.save.get_files() 
        self.assertEqual(len(files), 0)
