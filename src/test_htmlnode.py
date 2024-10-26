from htmlnode import HTMLNode
import unittest

class TestTextNode(unittest.TestCase):
    def test_parameters(self):
        node = HTMLNode("div", "hello world")

        self.assertEqual(node.tag,"div","Test Failed: tags are not equal.")
        
        self.assertEqual(node.value,"hello world","Test Failed: values are not equal.")

        self.assertEqual(node.children,None,"Test Failed: children are not equal.")

        self.assertEqual(node.props,None,"Test Failed: props are not equal.")


    def test_single_props(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        expected = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(),expected,
                         "Test Failed: Nodes are unequal.")


    def test_mult_props(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),expected,
                         "Test Failed: Nodes are unequal.")
        
    def test_empty_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(),'',
                         "Test Failed: Nodes are unequal.")
              
    def test_repr_eq(self):
        node = HTMLNode("a", "hello world", ["h1","p"],{"href": "https://www.google.com", "target": "_blank"})
        expected = "HTMLNode(a, hello world, children: ['h1', 'p'], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(expected, repr(node), "Test Failed")

    def test_repr_all_none(self):
        node = HTMLNode()
        expected = "HTMLNode(None, None, children: None, None)"
        self.assertEqual(expected, repr(node), "Test Failed")



if __name__ == "__main__":
    unittest.main()