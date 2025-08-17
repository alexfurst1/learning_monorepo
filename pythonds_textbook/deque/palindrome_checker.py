#this program is a recommended problem from the pythonds textbook in chapter 4.18

from deque import Deque

def is_palindrome(str: str) -> bool:
    myQue = Deque()
    
    for i in str:
        myQue.addRear(i)

    while myQue.size() > 1:
        if myQue.removeFront() != myQue.removeRear():
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("hannah"))

