
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
        self.draw_node = DrawNode()
        self.canvas = None
        self.create_widgets()
    

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Valitse väri")[1]
        if color_code:
            self.selected_color = color_code

    def create_widgets(self):
        self.canvas = Canvas(
            self, bg="white", width=800, height=600)
        self.canvas.pack(fill="both", expand=True, side="left")
        self.draw_node.draw_tree(self.canvas)

    def draw(self):
        self.draw_node.draw_tree(self.canvas)

def main():
    root = Tk()
    root.title("Kodokaze Canvas")
    app = MainApplication(master=root)
    app.mainloop()


# generoitu koodi päättyy
if __name__ == "__main__":
    main()
