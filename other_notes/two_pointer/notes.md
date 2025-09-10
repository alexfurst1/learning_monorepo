1. two pointers is an algorithm where you have two index variables in a data structure, and they move to search, sort, etc.

 - can bring complexity from O(n^2) to O(n)

 1. converging pointers:
  - pointers start at opposite sides of the list, and move towards eachother
  - common use is a palindrome checker, where if each pointer matches they move inwards

 2. parallel pointes
  - both pointers start at the beginning, and one follows behind the other
  - the right pointer usually explores and finds new information, while the left holds an index, range, or window
  - this is how sliding window works, where the range of i to j is fixed, and both pointers increment at the same time, kindof creating a window within a list to operate in or outside of
   - sliding window is helpful for substrings or subarrays
 
 3. trigger based pointers
  - both pointers start at the same end, and we move the right until a certain criteria is met where we can move the left pointer 