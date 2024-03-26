import htmlnode


class TextNode:
    def __init__(self, text="default", text_type="default_text_type", url=None, props=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.props = props

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url and
                self.props == self.props)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url}, {self.props})"




