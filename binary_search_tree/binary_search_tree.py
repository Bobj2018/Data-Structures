import json
from stack import Stack
from queue import Queue

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while node:
            if node.value == target:
                return True
            else:
                node = node.right
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        node = self

        while node is not None:
            if node.value > current_max:
                current_max = node.value
            node = node.right

        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        if self.left:
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)




    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()








    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)
        while len(queue) > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = Stack()
        s.push(self)

        while len(s) > 0:
            node = s.pop()

            print(node.value)

            if node.left:
                s.push(node.left)
            if node.right:
                s.push(node.right)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):

        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

    def __repr__(self):
        return f"BSTNode({self.value})"
"""
This code is necessary for testing the `print` methods
"""

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
print('***')
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
