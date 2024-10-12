import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2, "Test Passed: Nodes match.")

    def test_text_diff(self):
            node = TextNode("This is a text node", text_type_bold)
            node2 = TextNode("This is a text node2", text_type_bold)
            self.assertNotEqual(node, node2,
                                "Test Passed: Nodes are not equal - text is different.")

    def test_text_type_diff(self):
            node = TextNode("This is a text node", text_type_bold)
            node2 = TextNode("This is a text node", text_type_italic)
            self.assertNotEqual(node, node2,
                                "Test Passed: Nodes are not equal - text type is different.")

    def test_url_eq(self):
        node = TextNode("This is a text node", text_type_bold,"https://www.google.ie")
        node2 = TextNode("This is a text node", text_type_bold,"https://www.google.ie")
        self.assertEqual(node, node2,"Test Passed: Nodes are equal")

    def test_repr_eq(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.google.ie")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.google.ie)", repr(node), 
            "Test Passed")

    
if __name__ == "__main__":
    unittest.main()
