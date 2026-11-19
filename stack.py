class node:
    def __init__(self, value):
        self.data = value 
        self.next = None 

class stack:
    def __init__(self):
        self.top = None 

    def is_empty(self):
        return self.top is None 

    def push(self, new_node):
        new_node.next = self.top 
        self.top = new_node 

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        temp = self.top 
        self.top = temp.next
        temp.next = None
        print("Popped Elements : ", temp.data)
        return temp.data

    def print(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Stack contains :- ")
            temp = self.top 
            while temp:
                print(temp.data)
                temp = temp.next 

    def reverse(self):
        prev = None
        temp = self.top
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.top = prev


if __name__ == "__main__":
    sta = stack()
    sta.push(node(10))
    sta.push(node(20))
    sta.push(node(30))
    sta.push(node(40))
    sta.push(node(50))
    sta.print()
    sta.pop()
    sta.reverse()
    sta.print()