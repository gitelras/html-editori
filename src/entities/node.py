class Node:
    def __init__(self, size, is_vertical):
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
        self.children.append(child)
        child.parent = self
