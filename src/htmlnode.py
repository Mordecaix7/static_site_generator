class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return (self.tag == other.tag and self.value == other.value and
                self.children == other.children and self.props == other.props)

    def __repr__(self):
        return (f"HTMLNode: tag={self.tag}, value={self.value}, "
                f"children={self.children}, props={self.props}")

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            if type(self.props) is dict:
                if self.props == {}:
                    return ""
                # consider ensuring each value is enclosed with "" if it doesn't start with it.
                # Iterate through key: value pairs in props to generate html string.
                props_as_html = [f" {key}=\'{value}\'" for key, value in self.props.items()]
                # Join strings as single string for return. (Should be okay for 1 pair or more.)
                # Consider implementing a check to avoid an empty string return.
                props_as_html = ''.join(props_as_html)
                return props_as_html
            else:
                raise TypeError(f"self.props is type{type(self.props)} expected dict ")
        else:
            return ""


class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.tags = {
            None: lambda: self.value,
            "para": lambda: f"<p{self.props_to_html()}>{self.value}</p>",
            "bold": lambda: f"<b{self.props_to_html()}>{self.value}</b>",
            "ital": lambda: f"<i{self.props_to_html()}>{self.value}</i>",
            "code": lambda: f"<code{self.props_to_html()}>{self.value}</code>",
            # "<a href=\"https://www.ex.com\">This is a link</a>"
            "link": lambda: f"<a{self.props_to_html()}>{self.value}</a>",
            "img": lambda: f"<img src=\'{self.value}\'{self.props_to_html()}>"

        }

    def __repr__(self):
        return (f"LeafNode: value={self.value}, tag={self.tag}, "
                f"children={self.children}, props={self.props}")

    def to_html(self):

        if self.value is None:
            raise ValueError("self.value is not set.")
        elif type(self.tag) is str and self.tag not in self.tags:
            raise ValueError(f"{self.tag} not implemented in tags to html dictionary")
        else:
            return self.tags[self.tag]()


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(children=children, tag=tag, props=props)
        self.children_as_html = ""
        self.tags = {
            "para": lambda: f"<p{self.props_to_html()}>{self.children_as_html}</p>",
            "bold": lambda: f"<b{self.props_to_html()}>{self.children_as_html}</b>",
            "ital": lambda: f"<i{self.props_to_html()}>{self.children_as_html}</i>",
            "code": lambda: f"<code{self.props_to_html()}>{self.children_as_html}</code>",
            "link": lambda: f"<a{self.props_to_html()}>{self.children_as_html}</a>",
        }

    def __repr__(self):
        return (f"ParentNode: tag={self.tag}, props={self.props} "
                f"children={' '.join(repr(child) for child in self.children)}")

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is None")
        elif self.children is None:
            raise ValueError("No children")
        elif self.tag == "img":
            raise Exception("Error: img tag is self closing and can have no children")
        else:
            #for child in self.children:
            #    html = child.to_html()  # Call the method and store the result to inspect it
            #    print("HTML Result:", html, "Type:", type(html))
            #    assert isinstance(html, str), "Expected a string return value from to_html"

            #print("Testing Information =================")
            #for child in self.children:

            #    print(child, type(child.to_html))
            #print("Testing Information =================")
            self.children_as_html = ''.join(child.to_html() for child in self.children)
            return self.tags[self.tag]()
