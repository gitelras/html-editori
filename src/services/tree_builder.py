#from repositories.html_repository import Save
from entities.node import Node

class TreeBuilder:
    def __init__(self):
        self.text = ""

    def create_menu_tree(self):
        root = Node(100, True)
        node_a = Node(20, True)
        root.add_child(node_a)
        node_b = Node(80, False)
        root.add_child(node_b)
        node_e = Node(40, True)
        node_e.color = "red"
        node_a.add_child(node_e)
        node_c = Node(50, True)
        node_b.add_child(node_c)
        for _ in range(5):
            child_node = Node(10, True)
            child_node.color = "blue"
            node_c.add_child(child_node)
        node_d = Node(20, True)
        node_b.add_child(node_d)
        for _ in range(5):
            child_node = Node(5, True)
            child_node.color = "green"
            node_d.add_child(child_node)

        return root
