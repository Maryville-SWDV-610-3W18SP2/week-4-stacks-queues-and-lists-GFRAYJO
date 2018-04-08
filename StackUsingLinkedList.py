class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return True if self.head is None else False
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
            return
        popData = self.head.data
        self.head = self.head.next
        print((popData))
        
if __name__ == '__main__':
    
    stack = linkedList()
    
    stack.push(100)
    stack.push(200)
    stack.push(400)
    stack.push(800)
        
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
  
