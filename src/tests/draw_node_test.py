import unittest
import logging
from entities.node import Node
from tkinter import Tk, Canvas
from services.draw_node import DrawNode

class TestDrawnode(unittest.TestCase):
    def setUp(self):
        self.tk = Tk()
        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = Canvas(self.tk, width=800, height=600)
        self.canvas.pack()
        self.tk.update()
        self.draw_node = DrawNode(self.canvas)

    def test_draw_root_right(self):
        root = Node(100, True)
        root.color = "red"
        self.draw_node.draw_node(self.canvas, root, 0, 0, 800, 600)
        self.tk.update()
        all_items = self.canvas.find_all()

        for item_id in all_items:
            item_type = self.canvas.type(item_id)
            if item_type == 'rectangle':
                width, height = self.get_rectangle_size(self.canvas, item_id)
                self.assertEqual(width, 800, f"Leveyden tulisi olla 800, ei {width}")
                self.assertEqual(height, 600, f"Korkeuden tulisi olla 600, ei {height}")

    def get_rectangle_size(self, canvas, rectangle_id):
        x1, y1, x2, y2 = canvas.coords(rectangle_id)
        width = x2 - x1
        height = y2 - y1
        return width, height
    
    def test_click_right_node(self):
        pass

    def tearDown(self):
        self.tk.destroy()
