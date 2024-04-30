import unittest
from services.html_builder import HtmlBuilder
from entities.node import Node

class TestTreeBuilder(unittest.TestCase):
    def setUp(self):
        self.html_builder = HtmlBuilder()
        self.node = Node(100, True)
        self.node.color = "blue"
        self.node.text_color = "white"
        self.node.font = "Arial"
        self.node.font_size = 14
        self.node.text = "Root Node"
        self.node.children = []

    def test_generate_html_right(self):
        expected_html = (
            '<div style="position: absolute; left: 0%; top: 0%; width: 100%; height: 100%; '
            'background-color: blue; color: white; font-family: Arial; font-size: 14px; overflow: hidden;">'
            '<div style="position: relative; left: 10px; top: 10px;">Root Node</div>\n'
            '\n</div>'
        )
        actual_html = self.html_builder.generate_html(self.node)
        self.assertEqual(actual_html, expected_html)
