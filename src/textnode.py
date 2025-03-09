from enum import Enum 
from htmlnode import LeafNode

class TextType(Enum):
    TEXT    = "text"
    BOLD    = "bold"
    ITALIC  = "italic"
    CODE    = "code"
    LINK    = "link"
    IMAGE   = "image"

class TextNode():

    def __init__(self, text: str, text_type: TextType, url=None):
        
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text_type == other.text_type

    def __repr__(self):
        if self.url == None:
            return f"TextNode({self.text}, {self.text_type.value})"
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.Italic:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.URL:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMG:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")


