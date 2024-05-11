
from entities.node import Node

class TreeBuilder:
    """
    Luokka, joka rakentaa puurakenteen Node-solmuja käyttäen.

    """
    def __init__(self):
        pass

    def create_apple_tree(self):
        """
        Luo ja palauttaa puurakenteen.

        Returns:
            Node: Juurisolmu rakennetulle puulle, joka sisältää lapsia ja lapsenlapsia.
        """
        root = Node(100, False)

        node_a = Node(40, True)
        node_a.color = "#8687d0"
        root.add_child(node_a)
        node_b = Node(220, True)
        node_a.color = "#8687d0"
        root.add_child(node_b)
        node_e = Node(40, True)
        node_e.color = "#8687d0"
        root.add_child(node_e)

        for node in [node_a, node_b, node_e]:
            child_1 = Node(100, False)
            child_1.color = "#8687d0"
            child_2 = Node(200, False)
            child_2.color = "#8687d0"
            child_3 = Node(100, False)
            child_3.color = "#8687d0"
            node.add_child(child_1)
            node.add_child(child_2)
            node.add_child(child_3)

        return root

    def create_lemon_tree(self):
        """
        Luo ja palauttaa puurakenteen.

        Returns:
            Node: Juurisolmu rakennetulle puulle, joka sisältää lapsia ja lapsenlapsia.
        """
        root = Node(100, False)

        node_a = Node(40, True)
        node_a.color = "#8687d0"
        root.add_child(node_a)
        node_b = Node(100, True)
        node_a.color = "#8687d0"
        root.add_child(node_b)
        node_e = Node(40, True)
        node_e.color = "#8687d0"
        root.add_child(node_e)

        for node in [node_a, node_b, node_e]:
            child_1 = Node(100, False)
            child_1.color = "#8687d0"
            child_2 = Node(20, False)
            child_2.color = "#8687d0"
            child_3 = Node(100, False)
            child_3.color = "#8687d0"
            node.add_child(child_1)
            node.add_child(child_2)
            node.add_child(child_3)
      
        return root

    def create_menu_tree(self):
        """
        Luo ja palauttaa puurakenteen.

        Returns:
            Node: Juurisolmu rakennetulle puulle, joka sisältää lapsia ja lapsenlapsia.
        """
        root = Node(100, True)
        node_a = Node(20, True)
        root.add_child(node_a)
        node_b = Node(80, False)
        root.add_child(node_b)
        node_e = Node(40, True)
        node_e.color = "#8687d0"
        node_a.add_child(node_e)
        node_c = Node(50, True)
        node_b.add_child(node_c)
        for _ in range(5):
            child_node = Node(10, True)
            child_node.color = "#8687d0"
            node_c.add_child(child_node)
        node_d = Node(20, True)
        node_b.add_child(node_d)
        for _ in range(5):
            child_node = Node(5, True)
            child_node.color = "#8687d0"
            node_d.add_child(child_node)

        return root
