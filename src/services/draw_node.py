
from services.tree_builder import TreeBuilder

# generoitu koodi alkaa

class DrawNode:
    def __init__(self, canvas, entry, master=None):
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

    def get_active_node(self):
        return self.active_node

    def draw_tree(self):
        self.draw_node(self.canvas, self.root_node, 0, 0,
                       self.canvas_width, self.canvas_height)

    def on_canvas_click(self, event):
        print("LOL")
        print(f"Klikattiin koordinaateissa: ({event.x}, {event.y})")
        result_node = self.get_node(self.root_node, 0, 0,
                                    self.canvas_width, self.canvas_height, (event.x, event.y))
        if result_node:
            print(f"Klikattu solmu: {result_node}")
            print(result_node.color)
            self.active_node = result_node
        else:
            print("Klikkaus ei osunut mihinkään solmuun.")

    def on_entry_return(self, _):
        if self.active_node:
            print("Here we go")
            print(self.active_node.color)
            self.active_node.text_color = self.selected_color
            self.active_node.font_size = self.font_size
            self.active_node.font = self.font
            print(self.entry.get())
            self.active_node.text = self.entry.get()
            print(self.active_node.text)
            self.draw_tree()

    def get_node(self, node, x, y, width, height, click_point):
        if x <= click_point[0] <= x + width and y <= click_point[1] <= y + height:
            if not node.children:
                return node
            if node.vertical:
                child_y = y
                size_sum = sum(child.size for child in node.children)
                for child in node.children:
                    child_height = height * (child.size / size_sum)
                    result = self.get_node(child, x, child_y, width, child_height,
                                           click_point)
                    if result:
                        return result
                    child_y += child_height
            else:
                child_x = x
                size_sum = sum(child.size for child in node.children)
                for child in node.children:
                    child_width = width * (child.size / size_sum)
                    result = self.get_node(child, child_x, y, child_width, height,
                                           click_point)
                    if result:
                        return result
                    child_x += child_width
        return None

    def draw_node(self, canvas, node, x, y, width, height):
        print("tullaanko", node.color, node.text, node.font_size, node.font)
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
