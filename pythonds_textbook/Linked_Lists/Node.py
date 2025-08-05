# node class for linked lists implemented from scratch
# learning that i hate linked lists...

class Node:

    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,new_data):
        self.data = new_data

    def setNext(self,new_next):
        self.next = new_next

        