import unittest
import logging
from entities.node import Node
from tkinter import Tk, Canvas
from ui.experimental_gui import MainApplication 


class TestDrawnode(unittest.TestCase):
    def setUp(self):
        self.tk = Tk()
        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = Canvas(
            self.tk, width=self.canvas_width, height=self.canvas_height)
        self.app = MainApplication(master=self.tk, canvas_width=self.canvas_width, canvas_height=self.canvas_height)
        self.canvas.pack()

    def test_draw_root_right(self):
        root = Node(100, True)
        root.color = "red"
        all_items = self.app.canvas.find_all()
        self.app.draw_node(self.app.canvas, root, 0, 0, self.canvas_width, self.canvas_height)

        all_items = self.canvas.find_all()
        for item_id in all_items:
            logging.debug(item_id)
            item_type = self.canvas.type(item_id)
            if item_type == 'rectangle':
                self.get_rectangle_size(self.canvas, item_id)

    def get_rectangle_size(self, canvas, rectangle_id):
        x1, y1, x2, y2 = canvas.coords(rectangle_id)
        logging.debug(x1, y1, x2, y2)

        width = x2 - x1
        height = y2 - y1
        logging.debug(width, height)

        return width, height

    def test_draw_root_color(self):
        root = Node(100, True)
        root.color = "red"
        self.app.draw_node(self.app.canvas, root, 0, 0, self.canvas_width, self.canvas_height)

        all_items = self.canvas.find_all()
        for item_id in all_items:
            item_color = self.canvas.itemcget(item_id, "fill")
            self.assertEqual(item_color, "red",
                             f"Suorakulmion {item_id} väri pitäisi olla 'red'")

    def tearDown(self):
        self.tk.destroy()