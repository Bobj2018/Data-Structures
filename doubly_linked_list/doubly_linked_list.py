"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev_node = None, next_node = None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        tmp = self.head
        self.delete(self.head)
        return tmp.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #create a node passing the value as an argument
        node = ListNode(value)
        #check if tail is None
        if self.tail is None:
            self.head = node
            self.tail = node
        #set set tail.next to node
        else:
            self.tail.next = node
        #set node.prev to tail
            node.prev = self.tail
        #set the tail to the node
            self.tail = node
        self.length += 1



    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tmp = self.head
        self.delete(self.tail)
        return tmp.value



    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
