1. The bubble sort

the bubble sort makes multiple passes through a list, highlighting two adjacent items at a time, and swaps their position if they are out of order (usually numerical order). Each successive pass goes through n-1, since the last item is always going to be the largest. Each largest item of the sliced list will be bubbled to the end until all items are in order.

- apparently you can simultaneously swap variables in python.
 - this is done like this:
 x = 10
 y = 5
 x, y = y, x
 print(x) = 5
 print(y) = 10 
 - can be done with more than two variables as well, as long as the order is respective

- known as the most inefficient sorting method lmao
- however, if during a pass we know that there were no exchanges, we know the full list is sorted. This is something other algorithms lack the ability to do

2. Selection sort
the selection sort improves on the bubble sort, the difference being the selection sort makes only one exchange per pass.
- basically, each pass find the largest item in the list and moves it to the end. Just like the bubble sort, each successive pass iterates the length n-1 over the list. So, each sorted item remains at the end.

3. Insertion sort
O(n^2) just like the bubble, short bubble, and selection sorts, works in a slightly different way.
- it always retains a sorted sublist in the lower portions of the main list. Each new item is added to that sorted sublist in order, until the main list only contains the sorted sublist. 
 - each item immediately to the right of the sorted sublist is the item being handled. It is inserted by shifting all larger items in the sorted sublist to the right.

 4. Shell short (actually used irl)
 - is kind of like an add-on to the insertion sort to make it more efficient.
 1. first, it selects multiple sublists throughout the main list. It does this by selecting items with a fixed gap between them. For example a gap of 3 would select every 3rd item, and so every 3rd item would be the first sublist, started with item 0. Then, the next sublist would start at item 1, and so on, until every item exists within a sublist.
 2. it then sorts those individual sublists. This gives the insertion sort an advantage, since items of similar size are now clustered together.
  - you'd have more items around 10 at the beginning, and more items around 45 at the end, if you were to have a list with items ranging from 0-50 (45 is arbitrary)
  3. finally, an insertion sort is conducted, resulting in many less overrall shifts, resulting in much lower computing cost.

- can perform at O(n^(3/2))

5. Merge Sort
 - divide and conquer strategy
 - recursive algorithm that continually splits a list in half
 - it then loops through all items and adds them back up sorted
 - sort of hard to explain how it does it

 6. Quick sort
  - this algo uses divide and conquer as wel
  - uses less space than the merge sort
  - however, the list may not be divided in half at all, diminishing performance
  1. picks a pivot point (usually the first item)
  2. two pointers, at the left and right ends of the list, which move inward.
  3. the left moves until it finds an item larger than the pivot point, and the right moves until it finds an item smaller
  4. it then swaps those items, and continues until rightmark < leftmark, where rightmark becomes the partition point
  5. it then recursively splits the list in half, excluding the pivot point from both lists, and quicksorts both lists, until it adds everything up again

  - for a list of n items, if the partition is always in the middle, the result is (n log n)
  - however, worst case scenario is O(n^2)
  - when we use different methods to choose the pivot point, such as median of three, in some circumstances it can increase efficiency
   - median of three chooses the first, middle, and last element, then chooses the median to be the pivot point.

**Summary**

- the bubble, selection, and insertion sorts are O(n^2)
- a shell sort falls between O(n) and O(n^2)
- a merge sort is O(n log n) but requires additional space
- a quick sort is O(n log n) but may deteriorate to O(n^2) if the split points are not near the middle of the list. Does not require additional space