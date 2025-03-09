from enum import Enum 

class TextType(Enum):
    NORMAL  = "normal"
    BOLD    = "bold"
    ITALIC  = "italic"
    CODE    = "code"
    URL     = "url"
    IMG     = "img"

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text_type == other.text_type

    def __repr__(self):
        if self.url == None:
            return f"TextNode({self.text}, {self.text_type.value})"
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

