# this is a raw implementation of a deque data structure from memory.

class Deque:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
        
    def addFront(self,item):
        return self.items.insert(0,item)

    def addRear(self,item):
        return self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)
        