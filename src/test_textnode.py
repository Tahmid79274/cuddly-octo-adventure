import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,None)
        node2 = TextNode("This is a text node", TextType.BOLD,None)
        node3 = TextNode("This is an text node", TextType.BOLD,None)
        node4 = TextNode("This is text node", TextType.LINK,None)
        node5 = TextNode("This is text node", TextType.BOLD,None)
        node6 = TextNode("This is text node", TextType.BOLD,None)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node4)

if __name__ == "__main__":
    unittest.main()