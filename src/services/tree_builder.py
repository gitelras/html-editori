
from entities.node import Node

class TreeBuilder:
    """
    Luokka, joka rakentaa monimutkaisen puurakenteen Node-solmuja käyttäen.

    Attributes:
        text (str): Teksti, jota voidaan käyttää puun rakentamisessa (tässä esimerkissä ei käytetä).
    """

    def __init__(self):
        """
        Luo TreeBuilder-olion alustamalla teksti-attribuutin.
        """
        self.text = ""

    def create_menu_tree(self):
        """
        Luo ja palauttaa puurakenteen esimerkin.

        Tässä metodissa luodaan useita Node-olioita ja
        asetellaan ne hierarkkisesti vanhempi-lapsi -suhteisiin.
        Puu rakennetaan kiinteästi määritellyllä tavalla, 
        ja solmuille asetetaan eri värit tunnistamisen helpottamiseksi.

        Returns:
            Node: Juurisolmu rakennetulle puulle, joka sisältää lapsia ja lapsenlapsia.
        """
        root = Node(100, True)
        node_a = Node(20, True)
        root.add_child(node_a)
        node_b = Node(80, False)
        root.add_child(node_b)
        node_e = Node(40, True)
        node_e.color = "#bcebeb"
        node_a.add_child(node_e)
        node_c = Node(50, True)
        node_b.add_child(node_c)
        for _ in range(5):
            child_node = Node(10, True)
            child_node.color = "#bcebeb"
            node_c.add_child(child_node)
        node_d = Node(20, True)
        node_b.add_child(node_d)
        for _ in range(5):
            child_node = Node(5, True)
            child_node.color = "#bcebeb"
            node_d.add_child(child_node)

        return root
