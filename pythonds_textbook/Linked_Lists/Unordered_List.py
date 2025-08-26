from Node import Node

# I hate this so much

class Unordered_List:
    
    def __init__ (self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    # these next methods cover linked list traversal, a difficult topic for me (as of right now)

    def size(self):
        count = 0
        current = self.head
        
        while current != None:
            count += 1
            current = current.getNext()
        
        return count
    
    def search(self,item):
        isFound = False
        current = self.head

        while current != None and not isFound:
            if current.getData == item:
                isFound = True
            else:
                current = current.getNext()

        return isFound
    
    def remove(self,item): # i don't fully understand this but I will try to memorize and eventually it will click
        found = False
        current = self.head
        previous = None

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    
            
