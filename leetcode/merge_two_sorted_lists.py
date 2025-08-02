# Definition for singly-linked list.
from typing import Optional # imported this because it was recommended


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 or list2:
        if list1.val <= list2.val:
            temp = list1.next
            list1.next = list2
            list1.next.next = temp
            return self.mergeTwoLists(self.list1,self.list2.next)
        else:
            temp = list1
            list1 = list2
            list1.next = temp
            return self.mergeTwoLists(self.list1,self.list2.next)
        
    return list1
    

