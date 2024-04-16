from tkinter import Entry
from services.tree_builder import TreeBuilder


class DrawNode:
    def __init__(self):
        self.canvas_width = 800
        self.canvas_height = 600

# generoitu koodi alkaa
    def draw_tree(self, canvas, font_family, font_size, color):
        self.font_family = font_family
        self.font_size = font_size
        self.selected_color = color
        tree_builder = TreeBuilder()
        root_node = tree_builder.create_menu_tree()
        self.draw_node(canvas, root_node, 0, 0,
                       self.canvas_width, self.canvas_height)

    def draw_node(self, canvas, node, x, y, width, height):
        print("tullaanko")
        rect = canvas.create_rectangle(
            x, y, x + width, y + height, fill=node.color) # rectangle id
        entry = Entry(canvas, bd=2, width=10)
        entry.place(x=x+5, y=y+5)

        def save_text(_, self=self, entry=entry, x=x, y=y):
            canvas.create_text(x+10, y+10, text=entry.get(), anchor="nw",
                               fill=self.selected_color, font=(self.font_family, self.font_size))
            print(self.font_family, self.font_size, self.selected_color)

        entry.bind("<Return>", save_text)


        if node.children:
            if node.vertical:
                child_y = y
                size_sum = sum(child.size for child in node.children)
                for child in node.children:
                    child_height = height * (child.size / size_sum)
                    self.draw_node(canvas, child, x, child_y,
                                   width, child_height)
                    child_y += child_height
            else:
                child_x = x
                size_sum = sum(child.size for child in node.children)
                for child in node.children:
                    child_width = width * (child.size / size_sum)
                    self.draw_node(canvas, child, child_x,
                                   y, child_width, height)
                    child_x += child_width

# generoitu koodi päättyy
