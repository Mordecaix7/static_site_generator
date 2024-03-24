import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<faketag>", "bold")
        node2 = HTMLNode("<faketag>", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("<fake>", "bold", None, None)
        self.assertEqual(f"HTMLNode: tag=<fake>, value=bold, "
                         f"children=None, props=None", repr(node))


if __name__ == "__main__":
    unittest.main()
