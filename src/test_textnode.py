import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2, "Test Failed: Nodes are unequal.")

    def test_text_diff(self):
            node = TextNode("This is a text node", TextType.BOLD)
            node2 = TextNode("This is a text node2", TextType.BOLD)
            self.assertNotEqual(node, node2,
                                "Test failed: Nodes are not unequal.")

    def test_text_type_diff(self):
            node = TextNode("This is a text node", TextType.BOLD)
            node2 = TextNode("This is a text node", TextType.ITALIC)
            self.assertNotEqual(node, node2,
                                "Test failed: Nodes are not unequal.")

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,"https://www.google.ie")
        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.google.ie")
        self.assertEqual(node, node2,"Test Failed: Nodes are unequal.")

    def test_repr_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.ie")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.google.ie)", repr(node), 
            "Test Failed")

    
if __name__ == "__main__":
    unittest.main()
