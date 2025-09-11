# selection sort algorithm copied from the textbook

def selection_sort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        pos_of_max = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[pos_of_max]:
                pos_of_max = location
            
        temp = alist[fillslot]
        alist[fillslot] = alist[pos_of_max]
        alist[pos_of_max] = temp

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)

# still O(n^2), but usually performs better in benchmark studies regardless

