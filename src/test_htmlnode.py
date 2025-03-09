import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_params(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(str(node), str(node2))

    def test_repr_None(self):
        node = HTMLNode()
        node_string = "HTMLNode(None, None, None, None)"
        self.assertEqual(str(node), node_string)

    def test_props_to_html_with_href(self):
        # Test a node with an href property
        node = HTMLNode("a", "Click me!", None, {"href": "https://www.google.com"})
        assert node.props_to_html() == 'href="https://www.google.com"'

    def test_props_to_html_with_multiple_props(self):
        # Test a node with multiple properties
        node = HTMLNode(
            "a", 
            "Click me!",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        # Check output has both properties
        props_html = node.props_to_html()
        assert 'href="https://www.google.com"' in props_html
        assert 'target="_blank"' in props_html

    def test_props_to_html_with_no_props(self):
        # Test a node with no properties
        node = HTMLNode("p", "Hello, world!", None, None)
        assert node.props_to_html() == ""

    


if __name__ == "__main__":
    unittest.main()