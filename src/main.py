from textnode import TextNode
def main():
    dummy_node = TextNode("I am dummy node", "bold", "https://www.boot.dev")
    print(dummy_node.repr())

main()