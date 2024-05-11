from services.tree_builder import TreeBuilder
# generoitu koodi alkaa
class DrawNode:
    """
    Luokka, joka vastaa puun solmujen piirtämisestä.

    Attributes:
        master (Tk widget): Pääikkuna tai vanhempi widget, johon tämä komponentti kuuluu.
        canvas (Canvas): Canvas-objekti, johon solmut piirretään.
        canvas_width (int): Canvas-alueen leveys.
        canvas_height (int): Canvas-alueen korkeus.
        font (str): Oletusfontti tekstille.
        font_size (int): Oletusfonttikoko tekstille.
        selected_color (str): Valitun solmun tekstin väri.
        tree_builder (TreeBuilder): TreeBuilder-olio, joka luo solmupuun.
        root_node (Node): Puun juurisolmu.
        active_node (Node): Aktiivinen solmu, johon viimeksi on kohdistettu toiminto.
        entry (Entry): Syötekenttä, josta luetaan solmun teksti.
    """

    def __init__(self, canvas, entry, master=None):
        """
        Luo DrawNode-luokan instanssin.

        Args:
            canvas (Canvas): Canvas-objekti, johon solmut piirretään.
            entry (Entry): Syötekenttä, josta luetaan solmun teksti.
            master (Tk widget, optional): Pääikkuna tai vanhempi widget. Oletus on None.
        """
        self.master = master
        self.canvas = canvas
        self.canvas_width = 800
        self.canvas_height = 600
        self.font = "Helvetica"
        self.font_size = 12
        self.selected_color = "black"
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.tree_builder = TreeBuilder()
        self.root_node = self.tree_builder.create_menu_tree()
        self.active_node = None
        self.entry = entry

    def draw_layout(self, layout_name):
        """
        Piirtää puun canvakselle.

        Args:
            layout_name: Nimi, joka yksilöi layoutin.
        """
        trees = {"Layout 1": self.tree_builder.create_apple_tree,
                 "Layout 2": self.tree_builder.create_menu_tree,
                 "Layout 3": self.tree_builder.create_lemon_tree}
        self.root_node = trees[layout_name]()
        self.draw_tree()

    def draw_tree(self):
        """Piirtää koko solmupuun canvakselle."""
        self.draw_node(self.canvas, self.root_node, 0, 0,
                       self.canvas_width, self.canvas_height)

    def on_canvas_click(self, event):
        """
        Käsittelee canvas-alueen klikkaustapahtumat.

        Args:
            event (Event): Tapahtumaobjekti, joka sisältää klikkauksen tiedot.
        """
        result_node = self.get_node(self.root_node, 0, 0,
                                    self.canvas_width, self.canvas_height, (event.x, event.y))
        if result_node:
            self.active_node = result_node

    def on_entry_return(self, _):
        """
        Päivittää aktiivisen solmun tekstiä, fonttia ja tekstiväriä, 
        kun syötekentässä painetaan Enter.

        """
        if self.active_node:
            self.active_node.text_color = self.selected_color
            self.active_node.font_size = self.font_size
            self.active_node.font = self.font
            self.active_node.text = self.entry.get()
            self.draw_tree()

    def get_node(self, node, x, y, width, height, click_point):
        """
        Etsii rekursiivisesti solmun, johon klikkaus osui.

        Args:
            node (Node): Tarkasteltava solmu.
            x (int): Solmun x-koordinaatti canvaksella.
            y (int): Solmun y-koordinaatti canvaksella.
            width (int): Solmun leveys.
            height (int): Solmun korkeus.
            click_point (tuple): Klikkauksen koordinaatit (x, y).

        Returns:
            Node: Löydetty solmu tai None, jos solmua ei löydy.
        """
        if x <= click_point[0] <= x + width and y <= click_point[1] <= y + height:
            if not node.children:
                return node
            if node.vertical:
                child_y = y
                child_x  = x
            else:
                child_x = x
                child_y = y
            size_sum = sum(child.size for child in node.children)
            for child in node.children:
                if node.vertical:
                    child_height = height * (child.size / size_sum)
                    child_width = width
                else:
                    child_height = height
                    child_width = width * (child.size / size_sum)
                result = self.get_node(child, child_x, child_y,
                                       child_width, child_height, click_point)
                if result:
                    return result
                if node.vertical:
                    child_y += child_height
                else:
                    child_x += child_width
        return None

    def change_colors(self, node, color):
        """
        Vaihtaa puun solmujen värin.
        
        """
        node.color = color
        for child in node.children:
            self.change_colors(child, color)

    def change_backround_color(self, color_code):
        self.change_colors(self.root_node, color_code)
        self.draw_tree()

    def draw_node(self, canvas, node, x, y, width, height):
        """
        Piirtää yksittäisen solmun ja kaikki sen lapsisolmut rekursiivisesti.

        Args:
            canvas (Canvas): Canvas, johon solmu piirretään.
            node (Node): Piirrettävä solmu.
            x (int): Solmun x-koordinaatti canvaksella.
            y (int): Solmun y-koordinaatti canvaksella.
            width (int): Solmun leveys.
            height (int): Solmun korkeus.
        """
        canvas.create_rectangle(x, y, x + width, y + height, fill=node.color)
        canvas.create_text(x+10, y+10, text=node.text, anchor="nw",
                           fill=node.text_color, font=(node.font, node.font_size))

        if node.children:
            if node.vertical:
                child_y = y
                size_sum = sum(child.size for child in node.children)
                for child in node.children:
                    child_height = height * (child.size / size_sum)
                    self.draw_node(canvas, child, x, child_y, width, child_height)
                    child_y += child_height
            else:
                child_x = x
                size_sum = sum(child.size for child in node.children)
                for child in node.children:
                    child_width = width * (child.size / size_sum)
                    self.draw_node(canvas, child, child_x, y, child_width, height)
                    child_x += child_width

# generoitu koodi päättyy
