class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Linkedlist:
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

    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    def findmid_del(self):
        if self.head is None:
            print("List is empty")
            return

        temp = temp1 = self.head
        prev = None
        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next

        print("middle node: ", temp.data)
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
        temp.next = None

    def delfirst_last(self):
        if self.head is None:
            print("List is empty")
            return

        first = self.head
        if first.next is None:
            self.head = None
            return

        self.head = first.next
        first.next = None

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        last = temp.next
        temp.next = None
        last.next = None

    def print(self):
        print("List elements: ")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
