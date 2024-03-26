import textnode
import htmlnode


class Converter:
    def __init__(self):
        self.valid_types = {"text_type_text": "text",
                            "text_type_bold": "bold",
                            "text_type_italic": "ital",
                            "text_type_code": "code",
                            "text_type_link": "link",
                            "text_type_image": "img"
                            }

    def markdown_to_text_nodes(self, text_file):
        pass

    def text_node_to_html_node(self, text_node):
        if text_node.text_type not in self.valid_types:
            raise Exception(f"text_type: '{text_node.text_type}' of type \'{type(text_node.text_type)}\' "
                            f"cannot be used. Only text, bold, italic, code, link or images are acceptable.")
        else:
