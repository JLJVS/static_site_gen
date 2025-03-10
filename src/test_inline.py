import unittest
from textnode import TextNode, TextType
from inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links  # import your function
from inline import split_nodes_image, split_nodes_link, text_to_textnodes

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    
    def test_bold_delimiter(self):
        node = TextNode("Hello **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " text")
    
    def test_italic_delimiter(self):
        node = TextNode("Hello _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_extract_markdown_links_with_image_first(self):
        text = "Here's an ![image](https://example.com/img.png) followed by a [regular link](https://example.com) and another [link](https://boot.dev)"
        links = extract_markdown_links(text)
        self.assertListEqual([("regular link", "https://example.com"), ("link", "https://boot.dev")], links)

    def test_extract_markdown_images_with_multiple(self):
        text = "Multiple images: ![first](https://example.com/first.jpg) and ![second](https://example.com/second.png)"
        images = extract_markdown_images(text)
        self.assertListEqual([("first", "https://example.com/first.jpg"), ("second", "https://example.com/second.png")], images)

    def test_extract_markdown_links_special_characters(self):
        text = "Link with [special & chars!](https://example.com/path?query=value&more=stuff)"
        links = extract_markdown_links(text)
        self.assertListEqual([("special & chars!", "https://example.com/path?query=value&more=stuff")], links)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_image_no_images(self):
        node = TextNode(
            "This is text with no images at all",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [node],  # Should return the original node unchanged
            new_nodes,
        )

    

    def test_split_link_at_end(self):
        node = TextNode(
            "This is text with a link at the [end](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link at the ", TextType.TEXT),
                TextNode("end", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_link_empty_alt_text(self):
        node = TextNode(
            "This link has [](https://example.com) empty alt text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This link has ", TextType.TEXT),
                TextNode("", TextType.LINK, "https://example.com"),  # Empty alt text
                TextNode(" empty alt text", TextType.TEXT),
            ],
            new_nodes,
        )

    # Test for an empty string
    def test_empty_string(self):
        input_text = ""
        expected_output = []
        
        # Call the function
        result = text_to_textnodes(input_text)
        
        # Check if the output is correct
        assert result == expected_output

    # Test for a string with bold and italic formatting
    def test_mixed_formatting(self):
        input_text = "**Bold** text and _italic_!"
        expected_output = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" text and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode("!", TextType.TEXT),
        ]
        
        # Call the function
        result = text_to_textnodes(input_text)
        print(result)
        # Check if the output is correct
        assert result == expected_output