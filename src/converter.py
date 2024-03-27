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

    def new_node(self, content=[], node_type=None, url=None, props={}):
        node = {
            "content": content,
            "type": node_type,
            "url": url,
            "props": props,
        }
        return node

    def block_to_text_nodes(self, string, pos=0):
        node = {
            "content": [],
            "type": None,
            "url": None,
            "props": None,
        }

        while pos < len(string):

            result = self.starts_with_tag(string[pos:])
            if result[0] is not None:
                node["type"] = result[1]

        return node

    def starts_with_tag(self, string, pos):
        if type(string) is not str: # handle errors
            raise TypeError(f"{type(string)} is not a string.")
        if type(pos) is not int or pos < 0 or pos > len(string) - 1:
            raise ValueError(f"{pos} of type({type(pos)}) must be an int greater than 0 and less than length of string.")

        # Handle per symbol
        # Handle escape case, but in good format this shouldn't be an issue.
        # If the index is at the start of the string (not possible to be escaped) or is not escaped.
        if pos == 0 or (pos > 0 and string[pos-1] != "\\"):
            if string[pos] == "*" and string[pos+1] != "*":
                return True, "ital", pos + 1
                # Then this must be italic case.
            elif string[pos] == "_" and string[pos+1] != "_":
                return True, "ital", pos + 1
                # Then this must be italic case.
            elif string[pos] == "*" and string[pos+1] == "*":
                return True, "bold", pos + 2
                # Then this must be bold.
            elif string[pos] == "_" and string[pos+1] == "_":
                return True, "bold", pos + 2
                # Then this must be bold.
            elif string[pos] == "`" and string[pos+1] != "`":
                return True, "code", pos + 1
                # Then this must be code.
            elif string[pos] == "`" and string[pos:pos+3] == "```":
                return True, "code", pos + 3
                # then this must be code.
            elif string[pos] == "!" and self.find_link_or_img(string, pos) is not None:
                # then this must be an image.
                return
            elif string[pos] == "[" and self.find_link_or_img(string, pos) is not None:
                # then this must be a link.
                return
            else:
                return False, "text", pos


    def is_closing_tag(self):
        pass
        # If you reach the end of string/branch without needing to recurse, return node.
    def find_link_or_img(self, string, i):
        # check if img/link is present at i. If so, return the end index, value, and type. =
        type = None
        # First, check if current character is not-escaped.
        if i > 0 and string[i - 1] == "\\":
            return None
        # Now check if the pattern for a link or img is found.
        if string[i] == "[" and string[i-1] != "!":  # Look for a link in markdown format
            pattern = r'\[.*?\]\(.*?\)'
            type = "link"

        elif string[i] == "!" and (i + 1 < len(string) and string[i + 1] == "["):
            pattern = r'\!\[.*?\]\(.*?\)'
            type = "img"
        else:
            return None  # Not the start of a link or image

        # Use regex to search for a complete link or image pattern from index i
        match = re.search(pattern, string[i:])
        if match:
            # Calculate the end index of the pattern
            end_index = i + match.end() - 1
            # Return the end index and the matched slice
            return end_index, string[i:end_index + 1], type  # include the end char in slice
        else:
            return None




