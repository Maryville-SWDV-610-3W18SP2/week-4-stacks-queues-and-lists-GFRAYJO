class Node:
    """Implementing a Queue using a linked list"""
    
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self,newNode):
        self.next = newNode
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def enqueue(self,data):
        item = Node(data)
        listItem = self.head
        if listItem is None:
            self.head = item
        else:
            while listItem.get_next():
                listItem = listItem.get_next()
            listItem.set_next(item)
            
    def dequeue(self):
        listItem = self.head
        if listItem != None:
            self.head = listItem.get_next()
        else:
            print('Queue is empty')
            
    def __len__(self):
        return self.size
    
    def is_empty(self):
        if self.head == None:
            raise Empty('Queue is Empty')
        else:
            return False
        
    def print_queue(self):
        listItem = self.head
        self.newList = []
        while listItem:
            self.newList.append(listItem.get_data())
            listItem = listItem.get_next()
        print(self.newList)
        
if __name__ == '__main__':
    
    q = Queue()
        
    q.enqueue('food')
    q.enqueue('drinks')
    q.enqueue('music')
    q.enqueue('dancing')
    q.enqueue('singing')
    
    q.print_queue()
    
    q.dequeue()
    q.print_queue()
    
    print(len(q))
    
    print(q.is_empty())

    
        
