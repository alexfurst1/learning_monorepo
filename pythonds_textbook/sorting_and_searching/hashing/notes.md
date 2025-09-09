- hashing notes

- hash tables seem to be like lists at first, but are initialized as a list with all elements pointing to None
- The goal of hash tables is to **make searching possible in O(1) time**
- hash tables are loaded by using a hash function to determine where an element should go
 - the hash function will take any item in the collection and return an integer in the range of slot names, from 0 to m-1, m being the length of the hash table
  - our first function, AKA the **remainder method** takes an item and divides it by the table size, returning the remainder as the hash value: (h(item) = item % 11)
- the number of slots filled over the total slots is called the load factor, often being written as **λ = 6/11**
- then when we want to search, we simply use the hash function to compute the slot name, then check to see if there is an item there or not
- collisions can occur in hashing. since each slot can only contain one element, if two different numbers both point to the same slot after the hash function we run into a problem.
- a perfect hash function is one where each element maps to a unique slot. unfortunately there is so systematic way of achieving this, but there are functions that extend the remainder function

- folding method:
 - divides the item into equal size pieces (the last item may not be of equal size), which are then added together to create the hash value
 - for example, the phone number 436-555-4601 would be added up like 43 + 65 + 55 + 56 + 01, and we get 210. Then, 210 % 11 (given there are 11 elements) would give us 1, and go to slot 1.
 - theres also a function that reverses every other piece of the split up element before adding it all together that gives it one extra step of uniqueness.

- mid-square method:
- we square the item, then extract some portion of the resulting digits.
 - ex: given 44, we square it resulting in 1936, then extract the **middle** two digits, giving us 93, and then applying the remainder function (93%11) we get 5 as our hash value.

- hashing strings
- we hash strings by using each character as an ordinal value. For example the word cat, we use ord('c') = 99, ord('a') = 97, ord('t') = 116, and then we add them together (99+97+116) = 312. We then apply the remainder function to get our hash value.
 - note: anagrams will always have the same hash value. To combat this, we apply a weight factor to each positional value.
 - ex: 99 * 1, 97 * 2, 116 * 3, so 99 + 194 + 348 = 641, 641 % 11 = 3.

 - you can always come up with more steps to complicate your hash function to be more effective, but remember the hash function must be efficient so it does not become the dominant part of the search and storage process. If it takes more work to compute, it would make the whole process inefficient and you'd have better performance searching over a simple list in O(n) time.

 - collision resolution
  - this is how we solve the problem of two unique items being hashed to the same slot
  - one common method is to find another open slot for the item that caused the collision. we can do this by starting at the original hash position, and moving sequentially until we find the first open slot. this is called **open addressing**
   - by systematically visiting each slot one time, we are using an open addressing technique called **linear probing**
 - once we start inserting items using linear probing, it is essential we search for them the same way
 - if we search for an item at its appropriate slot, but that slot is taken by a different element due to open addressing, we must start a sequential search at next slot and continue until we find the item, or we find an open slot.

 - a disadvantage to linear probing is clustering. This is when many items of the same hash value have been inserted and they have all been open addressed to slots very close to the hash value slot. This means there is much ground to cover when sequentially searching, which will increase the complexity of the search. 
 - a way to deal with this is to skip slots when linear probing, which will evenly distribute the items. for example we can do a plus 3 probe which means we look at every third slot for the insertion.
 - another name for this whole process is rehashing.
 - note: if we use a skip value (plus 3 probe) the hash table needs to be the length of a prime number, so that every single slot gets visited eventually. Otherwise, part of the table would never be used. This is why we've been using m=11 in this example.

 - a variation of linear probing is called quadratic probing
 - instead of searching sequentially, and iterating by 1, we increment the hash value by 1,3,5,9, and so on.
 - So, if the hash value if h, the successive values are h+1, h+4, h+9, h+16, and so on.
  - in general the i will be i^2 rehash(pos) = (h + i^2)

- an alternative method for handling collisions is to have each slot hold a reference to a collection (or chain) of items. For example, slot one would hold a list of items containing for example 11, 22, and 44. Most slots would only hold a collection of 1 item. 
- I assume that when a slot holds a collection of multiple items, you would of course have to search inside that collection. Hopefully those collections would be very small, and the search inside would not be significant enough to impact the O(1) time to drastically.


