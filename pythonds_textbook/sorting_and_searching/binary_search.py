# implementation of binary search.

def binary_search(item,alist):
    first = 0
    last = len(alist) -1 
    found = False

    while not found and first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

