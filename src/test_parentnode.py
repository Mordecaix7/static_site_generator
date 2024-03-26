import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        dummy_twin_node = LeafNode("I am a node meant to be in both parents.", "para")
        node = ParentNode([dummy_twin_node], "para")
        node2 = ParentNode([dummy_twin_node], "para")
        self.assertEqual(node, node2)

    def test_repr(self):
        child_node1 = LeafNode("I am a baby node.")
        child_node2 = LeafNode("test_image.jpg", "img", {"alt": "I am baby img node"})
        node = ParentNode([child_node1, child_node2], "para")
        self.assertEqual("ParentNode: tag=para, props=None children=LeafNode: value=I am a baby node., "
                         "tag=None, children=None, props=None LeafNode: value=test_image.jpg, "
                         "tag=img, children=None, props={\'alt\': \'I am baby img node\'}", repr(node))

    def test_cases(self):
        leafnode1 = LeafNode("test_image.jpg", "img", {"alt": "I am baby img node"})
        leafnode2 = LeafNode("Google", "link", {"href": "https://www.google.com"})
        leafnode3 = LeafNode("I am plain text.", None, None)
        leafnode4 = LeafNode("For simplicity I am more plain text.", None)
        parent1 = ParentNode([leafnode1, leafnode2], "para", None)
        parent2 = ParentNode([leafnode3, leafnode4, parent1], "para",)
        self.assertEqual("<p>I am plain text.For simplicity I am more plain text."
                         "<p><img src=\'test_image.jpg\' alt=\'I am baby img node\'>"
                         "<a href=\'https://www.google.com\'>Google</a></p></p>", parent2.to_html())


if __name__ == "__main__":
    unittest.main()
