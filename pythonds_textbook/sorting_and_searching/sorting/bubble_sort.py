# bubble sort algorithm copied from textbook

def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(alist)

# the outer loop loops backwards until there are no more items left to sort
# it decreases the size of the list to be looped over, so you only loop over unsorted items

# the inner loop loops over all the unsorted from 0 to n-1 and bubbles the largest number to the front

# a visual representation of a bar graph being sorted is a great way to understand how it works

# Best Case: O(n)
# Average: O(n^2)
# Worst: O(n^2)