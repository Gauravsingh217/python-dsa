class node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next = None

    def delete(self, value):
        temp = self.head
        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("value is not present in the list")
            return

        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        temp.prev = None
        temp.next = None
