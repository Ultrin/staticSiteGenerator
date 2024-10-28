import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        text_node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_link(self):
        text_node = TextNode("This is an link node", TextType.LINK, "https://www.ultrin.ca/")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is an link node")
        self.assertEqual(html_node.props, {"href": text_node.url})

    def test_image(self):
        text_node = TextNode("This is an image node", TextType.IMAGE, "https://www.ultrin.ca/")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": text_node.url, "alt": text_node.text})





if __name__ == "__main__":
    unittest.main()