import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        assert node.props_to_html() == ' href="https://www.google.com"'

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_with_attributes(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.example.com", "class": "link"})
        # The order of attributes might vary, so you might need to adjust this
        self.assertEqual(node.to_html(), '<a href="https://www.example.com" class="link">Click me!</a>')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", {"src": "image.jpg", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="An image"></img>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    


if __name__ == "__main__":
    unittest.main()