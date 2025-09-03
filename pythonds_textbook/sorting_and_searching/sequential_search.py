# implementation of sequential search from memory

def sequential_search(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

# simple idea, just loop through the list and compare each element to the item param, return true once found
# does this return just the boolean value or the index of the item as well?
# maybe return the index instead of the boolean value for this case ^

# o(n) complexity
