# Linked list

An array has the problem of inserting a new element into the array because 
it has to move the entire array. Also, if you want to insert a new element,
and the capacity is full, it has to allocate a new memory and then copy the
array into it.

A linked list on the other hand stores values at random memory locations, but those
are linked by pointers. The first element will have a reference to the address of the 
next element.

- Insert Element at beginning = O(1)
- Delete Element at beginning = O(1)
- Insert/Delete element at the end/middle = O(n)

Linked list has two main benefits over an array:

- You don't need to pre-allocate space
- Insertion is easier

- Linked list travesal = O(n)
- Accessing element by value = O(n)

Big O complexity for different operations on Array and Linked list

| | Array | Linked list|
|--| ------| ----------|
| Indexing | O(1) | O(n) |
| Insert/Delete element at start | O(n) | O(1) |
| Insert/Delete element at end | O(1) - amortized | O(n) |
| Insert element in middle | O(n) | O(n) |

The downside of using a linked list instead of an array is that you use more than twice
of memory.

You can't index into a linked list. Therefore, you can't do binary search on a linked list.
