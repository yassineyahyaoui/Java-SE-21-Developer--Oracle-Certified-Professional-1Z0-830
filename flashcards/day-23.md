# Day 23 -- Collections (Part 3): Sorting and Advanced Ops

### Q: What ordering do HashSet, LinkedHashSet, and TreeSet guarantee?
HashSet: no order. LinkedHashSet: insertion order. TreeSet: sorted order (natural or comparator).

### Q: What is the Queue interface and what principle does it follow?
Queue extends Collection and holds elements in FIFO (first-in, first-out) order. Insert at end, remove from front.

### Q: Which classes are commonly used to implement the Queue interface?
PriorityQueue and LinkedList. LinkedList implements Deque, which extends Queue, so it can be used as a Queue.

### Q: What is the difference between add() and offer() when adding to a Queue?
add() throws an exception if the element cannot be added; offer() returns false (or null) and does not throw, so the app does not crash.

### Q: What is the difference between remove() and poll() when removing from a Queue?
remove() throws NoSuchElementException if the queue is empty; poll() returns null. Prefer poll() to avoid crashes when the queue might be empty.

### Q: What is the difference between element() and peek() when retrieving the head of a Queue?
element() throws NoSuchElementException if empty; peek() returns null. Use peek() when the queue might be empty.

### Q: What is a Deque and how does it differ from a Queue?
Deque is a double-ended queue: you can add and remove from both ends. It supports both FIFO and LIFO. Found in java.util.

### Q: Which classes implement the Deque interface?
ArrayDeque and LinkedList. ArrayDeque is often used as a stack (push/pop/peek) or as a queue (offer/poll/peek).

### Q: How do you use a Deque as a stack?
Use push(e) to add at the front, pop() to remove from the front, peek() to view the front. LIFO.

### Q: Is Map part of the Collection framework?
No. Map is in java.util and is separate from the Collection hierarchy. It stores key-value pairs, not single elements.

### Q: How do HashMap, LinkedHashMap, and TreeMap differ in ordering?
HashMap: no guaranteed order. LinkedHashMap: insertion order. TreeMap: sorted by key (natural or comparator).

### Q: How do you add and retrieve entries in a Map?
put(key, value) to add or update; get(key) to retrieve the value. Duplicate keys overwrite the previous value.

### Q: What happens if you put two entries with the same key in a Map?
The second put overwrites the value for that key. The map contains only one entry per key.

### Q: How do you iterate over keys and values in a Map?
Use map.keySet() to iterate keys and then get(value) for each, or use map.entrySet() and Map.Entry's getKey() and getValue().

### Q: How do you get descending order from a TreeMap?
Use descendingKeySet() for keys in descending order, or descendingMap() for a view of the map with keys largest to smallest.

### Q: What methods can alter or remove Map entries?
replace(key, newValue) to change a value; remove(key) to remove the entry for that key.
