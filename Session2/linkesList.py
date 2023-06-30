class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class LinkesList:
    def __init__(self):
        self.head=None

    def add_from_end(self,data):
        new_node=Node(data)
        if not self.head:
            
