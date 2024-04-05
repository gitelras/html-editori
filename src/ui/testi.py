from tkinter import Tk, Canvas
from typing import List
from entities.node import Node
from services.tree_builder import Tree_Builder

# generoitu koodi alkaa
def draw_node(canvas, node, x, y, width, height):
    """
    Piirtää annetun solmun ja kaikki sen lapsisolmut rekursiivisesti.
    """
    # Piirrä tämänhetkinen solmu
    canvas.create_rectangle(x, y, x + width, y + height, fill=node.color)
    
    if not node.children:
        return
    
    if node.vertical:
        # Jaetaan korkeus lasten kesken
        child_y = y
        size_sum = 0
        for child in node.children:
            size_sum += child.size
        for child in node.children:
            child_height = height * (child.size / size_sum)
            draw_node(canvas, child, x, child_y, width, child_height)
            child_y += child_height
    else:
        # Jaetaan leveys lasten kesken
        child_x = x
        size_sum = 0
        for child in node.children:
            size_sum += child.size
        for child in node.children:
            child_width = width * (child.size / size_sum)
            draw_node(canvas, child, child_x, y, child_width, height)
            child_x += child_width

def main():
    root = Tk()
    root.title("HTML Document Tree Visualizer")

    canvas_width = 800
    canvas_height = 600
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Rakenna puu esimerkiksi
    tree_builder = Tree_Builder()
    root_node = tree_builder.create_menu_tree()

    # Piirrä puu
    draw_node(canvas, root_node, 0, 0, canvas_width, canvas_height)

    root.mainloop()

if __name__ == "__main__":
    main()
# generoitu koodi päättyy