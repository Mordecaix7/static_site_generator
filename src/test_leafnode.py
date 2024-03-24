import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("para", "I am a paragraph")
        node2 = LeafNode("para", "I am a paragraph")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = LeafNode("I am a paragraph", "para")
        self.assertEqual(f"LeafNode: value=I am a paragraph, tag=para, "
                         f"children=None, props=None", repr(node))

    def test_html(self):
        testing = {
            # tag type
                # arguments to pass into node creation
                # string to check output against
            "text": {
                "node_creation": ["I am plain text", None, None],
                "output_validation": "I am plain text"
            },
            "para": {
                "node_creation": ["I am a paragraph", "para", None],
                "output_validation": "<p>I am a paragraph</p>"
            },
            "ital": {
                "node_creation": ["I am italicized text", "ital", None],
                "output_validation": "<i>I am italicized text</i>"
            },
            "code": {
                "node_creation": ["This is a line of code", "code", None],
                "output_validation": "<code>This is a line of code</code>"
            },
            "link": {
                "node_creation": ["This is a link", "link", {"href": "https://www.ex.com"}],
                "output_validation": "<a href=\"https://www.ex.com\">This is a link</a>"
            },
            "img": {
                "node_creation": ["image.jpg", "img", {"alt": "Alt text"}],
                "output_validation": "<img src=\"image.jpg\" alt=\"Alt text\">"
            }

        }
        # test above cases. Use subtest.
        for tag, details in testing.items():
            with self.subTest(tag=tag):
                # Extract arguments
                node_arguments = details["node_creation"]
                # Create LeafNode
                test_node = LeafNode(*node_arguments)  # Unpack arguments
                # HTML output
                expected_output = details["output_validation"]
                # Compare method against expected output
                self.assertEqual(test_node.to_html(), expected_output)


if __name__ == "__main__":
    unittest.main()
