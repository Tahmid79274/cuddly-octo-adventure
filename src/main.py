from textnode import TextNode, TextType


def main():
    textNode = TextNode('This is some anchor text', 'link', url='https://www.boot.dev')
    print(textNode)


main()