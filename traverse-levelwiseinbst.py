class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0
        self.lcnt = 0
        self.nlcnt = 0

    def insert(self, new_node):
        if self.root is None:  # BST is empty
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:  # left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:  # right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # def del_node(self, rt, val):
    #     if rt is None:
    #         return rt
    #     if val<rt.data:
    #         rt.left=self.del_node(rt.left, val)
    #     elif val>rt.data:
    #         rt.right=self.del_node(rt.right, val)
    #     else:
    #         if rt.left is None: #Node with right child only
    #             return rt.right
    #         if rt.right is None: #Node with left child only
    #             return rt.left
    #         #Node has both left and right children
    #         succ=self.get_successor(rt)
    #         rt.data=succ.data
    #         rt.right=self.del_node(rt.right, succ.data)
    #     return rt

    # def get_successor(self, temp):
    #     temp=temp.right
    #     while temp.left is not None:
    #         temp=temp.left
    #     return temp

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is None and rt.right is None:
                self.lcnt += 1
            else:
                self.nlcnt += 1
            self.cnt += 1
            self.inorder(rt.right)


    def level_order(self,rt):
        if rt is None:
            print("bst is empty")
            return
        arr = []
        cnt = 0 # for counting the visited nodes
        arr.append(rt)
        while cnt<len(arr):
            temp=arr[cnt]
            cnt+=1
            print(temp.data,end=" ")
            if temp.left:
                arr.append(temp.left)
            if temp.right:
                arr.append(temp.right)   

b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
print("\nInorder Traversal: ", end=" ")
b1.inorder(b1.root)
print("\nLevel Order Traversal: ", end=" ")
b1.level_order(b1.root)
print()