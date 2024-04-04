from repositories.html_repository import Save
from entities.node import Node

class tree_builder:
    def __init__(self):
        self.text = ""

    def create_menu_tree(self):
        root = Node()
        node_A = Node()
        root.add_child(node_A)
        node_B = Node()
        root.add_child(node_B)
        node_E = Node()
        node_A.add_child(node_E)
        

        return root
    

    def import_text(self, text):
        self.text = text
        print(self.text)