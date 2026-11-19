class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node

        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        temp = self.front
        print("deleted node: ", temp.data)
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        temp.next = None
        return temp.data

    def print(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(temp.data, end='->')
            temp = temp.next