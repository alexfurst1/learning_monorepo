# raw implementation of sequential search of a list in ascending order from memory

def sequential_search(alist,item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos + 1

    return found

# still O(n), but average case is a little better. However, worst case is still O(n), making the whole algorithm O(n)