from repositories.html_repository import Save
from entities.node import Node

class Tree_Builder:
    def __init__(self):
        self.text = ""

    def create_menu_tree(self):
        root = Node(100,True)
        node_A = Node(20,True) 
        root.add_child(node_A)
        node_B = Node(80, False)
        root.add_child(node_B)
        node_E = Node(40, True)
        node_E.color = "red"
        node_A.add_child(node_E)
        node_C = Node(50, True)
        node_B.add_child(node_C)
        for i in range(5):
            child_node = Node(10, True)
            child_node.color = "blue"
            node_C.add_child(child_node)
        node_D = Node(20, True)
        node_B.add_child(node_D)
        for i in range(5):
            child_node = Node(5, True)
            child_node.color = "green"
            node_D.add_child(child_node)

        return root
    

    def import_text(self, text):
        self.text = text
        print(self.text)