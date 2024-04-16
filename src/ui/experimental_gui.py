
from tkinter import Tk, Canvas, Entry, Frame, Button, OptionMenu, StringVar, colorchooser
from typing import List
from entities.node import Node
from services.tree_builder import TreeBuilder
from services.draw_node import DrawNode
# generoitu koodi alkaa

class MainApplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.selected_color = "black"
        self.font_family = "Helvetica"
        self.font_size = 12
        self.draw_node = DrawNode()
        self.canvas = Canvas(self, bg="white", width=800, height=600)
        self.canvas.pack(fill="both", expand=True, side="left")
        self.create_widgets()
        self.draw()

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Valitse väri")[1]
        if color_code:
            self.selected_color = color_code
            self.draw()

    def create_widgets(self):
        font_family_var = StringVar(self)
        fonts = ["Times New Roman", "Arial", "Georgia", "Garamond", "Courier"]
        font_family_var.set(self.font_family)
        self.font_menu = OptionMenu(self, font_family_var, *fonts, command=self.update_font_family)
        self.font_menu.pack(side="top", fill="x")

        font_size_var = StringVar(self)
        font_size_var.set(str(self.font_size))
        self.font_size_menu = OptionMenu(self, font_size_var, *(str(x) for x in range(8, 49, 2)), command=self.update_font_size)
        self.font_size_menu.pack(side="top", fill="x")

        self.color_button = Button(self, text="Valitse väri", command=self.choose_color)
        self.color_button.pack(side="top", fill="x")

    def update_font_family(self, new_family):
        self.font_family = new_family
        self.draw()

    def update_font_size(self, new_size):
        self.font_size = int(new_size)
        self.draw()

    def draw(self):
        self.draw_node.draw_tree(self.canvas, self.font_family, self.font_size, self.selected_color)


def main():
    root = Tk()
    root.title("Kodokaze")
    app = MainApplication(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()

# generoitu koodi päättyy

