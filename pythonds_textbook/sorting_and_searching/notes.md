- chapter 6 of the textbook

1. Objectives (these are gathered from the textbook, but are going to be my way of recognizing if I have learned the material or not)
 - to be able to explain and implement sequential search and binary search
 - to be able to explain and implement selection sort, bubble sort, merge sort, quick sort, insertion sort, and shell sort
 - to understand the idea of hashing as a search technique
 - to introduce the map abstract data type
 - to implement the map abstract data type using hashing

 wow!

 2. Searching

 - python already has an easy way to search for an item in a dataset:
 - ex: 15 in [1,2,3]
  - False
 - however, we are interested in the underlying process of this

 - when data items are stored in a collection, we say they either have a sequential or linear relationship.
 - in a python list, elements can be accessed by their index, so we say they are stored sequentially

  1. sequential search

  easy, is exactly as it sounds

  2. binary search

   - starts with an element in the middle of an **ordered list,** compares it to the searched item, and cuts the searched list in half depending on if the middle element is higher / lower than the searched item\
   - great example of a divide and conquer strategy
   - O(log n) complexity
