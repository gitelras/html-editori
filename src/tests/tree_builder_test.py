import unittest
from services.tree_builder import TreeBuilder

class TestTreeBuilder(unittest.TestCase):
    def setUp(self):
        self.tree_builder = TreeBuilder()

    def test_build_root_right(self):
        root = self.tree_builder.create_menu_tree()
        self.assertEqual(root.size, 100)
        self.assertEqual(root.color, "white")
        self.assertTrue(root.vertical)
        self.assertEqual(len(root.children), 2)




