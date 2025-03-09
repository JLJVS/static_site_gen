from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    t = TextNode("Anchor text", TextType.URL, "https://www.boot.dev")
    print(t)
    node = HTMLNode("a", "Click me!", None, {"href": "https://www.google.com"})
    print(node.props_to_html())

main()