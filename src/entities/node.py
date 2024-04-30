class Node:
    """
    Edustaa yksittäistä solmua puurakenteessa. 
    Solmu voi sisältää lapsisolmuja ja se voi olla joko pysty- tai vaakasuuntainen.

    Attributes:
        vertical (bool): Tieto siitä, onko solmun lapsisolmut aseteltu 
        pysty- (True) vai vaakasuuntaan (False).
        children (list of Node): Lista lapsisolmuista.
        parent (Node): Viittaus vanhempaan solmuun. None, jos solmu on juuri.
        size (int): Solmun koko, joka vaikuttaa sen esityskokoon.
        color (str): Solmun taustaväri.
        text_color (str): Solmun tekstin väri.
        text (str): Solmussa näytettävä teksti.
        font (str): Tekstin fontti.
        font_size (int): Tekstin fonttikoko.
    """

    def __init__(self, size, is_vertical):
        """
        Luo uuden solmun.

        Args:
            size (int): Solmun koko, joka vaikuttaa sen esityskokoon.
            is_vertical (bool): Tieto siitä, onko solmun lapsisolmut aseteltu 
            pysty- vai vaakasuuntaan.
        """
        self.vertical = is_vertical
        self.children = []
        self.parent = None
        self.size = size
        self.color = "white"
        self.text_color = "blue"
        self.text = ""
        self.font = ""
        self.font_size = 10

    def add_child(self, child):
        """
        Lisää uuden lapsisolmun tähän solmuun.

        Args:
            child (Node): Lisättävä lapsisolmu.
        """
        self.children.append(child)
        child.parent = self
