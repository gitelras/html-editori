
from tkinter import Tk, Canvas, Entry, Frame, Button, OptionMenu, StringVar, colorchooser
from typing import List
from entities.node import Node
from services.tree_builder import Tree_Builder
# generoitu koodi alkaa
class MainApplication(Frame):
    def __init__(self, master=None, canvas_width=800, canvas_height=600):
        super().__init__(master)
        self.master = master
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.pack(fill="both", expand=True)
        self.create_widgets()
        self.selected_color = "black"

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Valitse väri")[1]
        if color_code:
            self.selected_color = color_code

    def create_widgets(self):
        self.canvas = Canvas(self, bg="white", width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(fill="both", expand=True, side="left")
        self.draw_tree()

    def draw_tree(self):
        tree_builder = Tree_Builder()
        root_node = tree_builder.create_menu_tree()
        self.draw_node(self.canvas, root_node, 0, 0, self.canvas_width, self.canvas_height)

    def draw_node(self, canvas, node, x, y, width, height):
        rect = canvas.create_rectangle(x, y, x + width, y + height, fill=node.color, outline="black")
        entry = Entry(canvas, bd=2, width=10)
        entry.place(x=x+5, y=y+5)  # Sijoitetaan Entry 5 pikseliä suorakulmion vasemmasta ja yläreunasta

        def save_text(event, self=self, entry=entry, x=x, y=y):
            canvas.create_text(x+10, y+10, text=entry.get(), anchor="nw", fill=self.selected_color, font=("Helvetica", 12))

        entry.bind("<Return>", save_text)  # Kun käyttäjä painaa Enter, teksti tallennetaan ja näytetään canvasilla

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

def main():
    root = Tk()
    root.title("Kodokaze Canvas")
    app = MainApplication(master=root)
    app.mainloop()

# generoitu koodi päättyy
if __name__ == "__main__":
    main()
