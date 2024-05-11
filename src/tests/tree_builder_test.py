import unittest
from services.tree_builder import TreeBuilder

class TestTreeBuilder(unittest.TestCase):
    def setUp(self):
        self.tree_builder = TreeBuilder()

    def test_build_vertical_root_right(self):
        root = self.tree_builder.create_menu_tree()
        self.assertEqual(root.size, 100)
        self.assertEqual(root.color, "white")
        self.assertTrue(root.vertical)
        self.assertEqual(len(root.children), 2)

    def test_build_horisontal_root_right(self):
        root = self.tree_builder.create_lemon_tree()
        self.assertEqual(root.size, 100)
        self.assertEqual(root.color, "white")
        self.assertFalse(root.vertical)

    def test_root_children(self):
        root = self.tree_builder.create_apple_tree()
        self.assertEqual(len(root.children), 3)
