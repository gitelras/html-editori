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
        self.draw_node = DrawNode(self.canvas, None)
        self.node = Node(100, True)
        self.node_child = Node(20, True)
        self.node_horisontal_child = Node(80, False)

    def test_draw_root_right(self):
        self.node.color = "red"
        self.draw_node.draw_node(self.canvas, self.node, 0, 0, 800, 600)
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
    
    def test_click_root_node(self):
        result = self.draw_node.get_node(self.canvas, self.node, 0, 0, self.canvas_width, self.canvas_height, 524, 66)
        self.assertEqual(self.node, result)
    
    def test_click_child_node(self):
        self.node.add_child(self.node_child)
        result = self.draw_node.get_node(self.canvas, self.node, 0, 0, self.canvas_width, self.canvas_height, 524, 66)
        self.assertEqual(self.node_child, result)

    def test_click_horisontal_node(self):
        self.node.vertical = False
        self.node.add_child(self.node_child)  
        self.node.add_child(self.node_horisontal_child) 
        self.node_horisontal_child.vertical = False
        result = self.draw_node.get_node(self.canvas, self.node, 0, 0, self.canvas_width, self.canvas_height, 489, 201)
        self.assertEqual(self.node_horisontal_child, result)

    def tearDown(self):
        self.tk.destroy()
