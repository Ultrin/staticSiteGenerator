from htmlnode import LeafNode
import unittest

class TestTextNode(unittest.TestCase):
    def test_just_text(self):
        node = LeafNode("Plain text", None)
        expected = "Plain text"
        self.assertEqual(node.to_html(), expected, "Test Failed: node didn't match expected.")

    def test_no_props(self):
        node = LeafNode("Hello world", "p")
        expected = "<p>Hello world</p>"
        self.assertEqual(node.to_html(), expected, "Test Failed: node didn't match expected.")

    def test_single_props(self):
        node = LeafNode("Click me!", "a", {"href": "https://example.com"})
        expected = '<a href="https://example.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected, "Test Failed: node didn't match expected.")

    def test_multiple_props(self):
        node = LeafNode("Input", "input", {"type": "text", "id": "username"})
        expected = '<input type="text" id="username">Input</input>'
        self.assertEqual(node.to_html(), expected, "Test Failed: node didn't match expected.")

    def test_no_value(self):
        node = LeafNode(None, "p")
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()