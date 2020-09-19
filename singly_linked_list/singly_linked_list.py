class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node

    def __repr__(self):
        return f"Node({self.get_value}, {self.get_next_node}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.set_next_node(self.head)
            self.head = node


    def add_to_tail(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next_node(node)
            self.tail = node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()

            return value

    def remove_tail(self):
        if self.tail is None:
            return None
        else:
            value = self.tail.get_value()
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                temp_node = self.head
                while temp_node.get_next_node() is not self.tail:
                    temp_node = temp_node.get_next_node()
                temp_node.set_next_node(None)
                self.tail = temp_node
            return value

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                return True
            else:
                current_node = current_node.get_next_node()
        return False

    def max(self):
        result = 0
        current_node = self.head
        while current_node is not None:
            if (current_node.get_value() > result):
                result = current_node.get_value()
            current_node = current_node.get_next_node()
        return result

    def __repr__(self):
        return f"LinkedList({self.head}, {self.tail})"
