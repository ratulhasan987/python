# tree practice

""" 
            7
         /     \
        2       4
       / \       \
      5   3       8
         / \     / \
        10   6  9   1

"""

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node
    def add_right(self, node):
        self.right = node

def create_tree():
    seven = Node(7)
    two = Node(2)
    four = Node(4)
    seven.add_left(two)
    seven.add_right(four)

    five = Node(5)
    three = Node(3)
    two.add_left(five)
    two.add_right(three)

    ten = Node(10)
    six = Node(6)
    three.add_left(ten)
    three.add_right(six)

    eight = Node(8)
    four.add_right(eight)

    nine = Node(9)
    one = Node(1)
    eight.add_left(nine)
    eight.add_right(one)
    # return root node
    return seven


def pre_order(node):
    print(node.item, end=' ')
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.item, end=' ')

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node.item, end=' ')
    if node.right:
        in_order(node.right)

if __name__ == "__main__" :
    Tree = create_tree()
    print(Tree.item)

    pre_order(Tree)
    print('\n')
    post_order(Tree)
    print('\n')
    in_order(Tree)

