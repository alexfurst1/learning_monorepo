# Understanding linked lists better for unordered lists
## don't know why I'm so bad at these...

- isEmpty method:
 - checks if the first node points to anything

- add method
 - since the list is unordered, we add new nodes to the easiest spot - the front
  - when adding items sequentially, you end up getting the list reversed of the order you added them
 1. creates a new node and sets the item param as it's data
 2. sets the new node's next value to the head's value
 3. sets the head as the new node
 - I keep remembering this backwards for some reason. Need to memorize

- size method
 - need to traverse the linked list, and keep a count of the number of nodes visited
 - current is a node set as the head, and is our sentinal value for our while loop (if that makes sense)
 - as long as current != None (current has to be equal to a node object, or else we know that there is no node and that is the end of the list), we continue the traversal
 - returns count (duh)

- search method
 - similar to size method
 - isFound variable to check if we found the item in question
 - current is again set to head
 - we loop through while current exists, and while the item is not found
 - if we find the item, we return the boolean
 - if we don't, current iterates to the the next node
 - if we can't find the item we return false

 - remove method
  - similar to search
  - we assume the value exists within the list, so we don't use current != None in our while loop condition
   - how to remove:
    1. use two external references to the current and previous node (since we can't traverse backwards)
    2. if the item is not found, previous must be set to current, and then current set to current.getNext(). This order is CRUCIAL and is called inchworming
    3. There are two scenarios once the item is found:
     1. the item in question is the head of the list
      - here we need to check if previous == None and if so,
      1. we set the head to current.getNext(), which remvoes current from the list
     2. the item is not the head
      - this is every other scenario, so we:
       1. set previous.next to current.getNext(), which then again wipes out current

       
    