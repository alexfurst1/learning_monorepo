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