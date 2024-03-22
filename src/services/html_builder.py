from repositories.html_repository import Save
from entities.node import Node

class HTML_builder:
    def __init__(self):
        self.text = ""
        root = Node()

    def add_child(self, parent):
        parent.children.append(Node())

    def import_text(self, text):
        self.text = text
        print(self.text)