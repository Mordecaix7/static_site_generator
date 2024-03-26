import textnode
import htmlnode
import re


class Converter:
    def __init__(self):
        self.valid_types = {"text_type_text": "text",
                            "text_type_bold": "bold",
                            "text_type_italic": "ital",
                            "text_type_code": "code",
                            "text_type_link": "link",
                            "text_type_image": "img"
                            }

    def markdown_to_blocks(self, text_file):
        # Convert entire markdown file into text nodes via regex.
        blocks = re.split(r'\n{2,}', text_file)
        return blocks

    def block_to_text_nodes(self, block):
        blockhandler = BlockHandler()
        blocks_as_text_nodes = []
        pass


    def text_node_to_html_node(self, text_node):
        # convert a single text_node into its corresponding html node.
        if text_node.text_type not in self.valid_types:
            raise Exception(f"text_type: '{text_node.text_type}' of type \'{type(text_node.text_type)}\' "
                            f"cannot be used. Only text, bold, italic, code, link or images are acceptable.")
        else:
            return

class BlockHandler:
    def __init__(self):
        self.blocks = []


    def get_blocks(self, blocks):
        self.blocks = blocks

    def blocks_to_text_nodes(self):
        blocks_as_text_nodes = [self.block_to_text_nodes(block) for block in self.blocks]
        return blocks_as_text_nodes

    def block_to_text_nodes(self, block):
        tag_stack = []
        block_as_text_node = None
        for index, character in enumerate(block):
        # Initialize block.
        # If it does not start with a tag set block_as_text_node = ["", "text"].
        # Append ["text", index] to tag_stack.
        # If the following characters are not an opening tag, concatenate the character to block_as_text_node[0]
        # If no tags are found by the end of the string, pop text tag from stack.
        # Else

        # Iterate through string.
        # Check if there is an opening tag.
        #

        return

    def starts_with_tag(self):




