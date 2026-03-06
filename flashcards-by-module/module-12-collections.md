# Module 12 -- Collections

### Q: What is the root of the Java Collections Framework?
The Collection interface is the root for most collections. List, Set, Queue, and Deque extend it. Map is separate (key-value, not a Collection).

### Q: What is the List interface and its main properties?
List is an ordered collection that allows duplicates. It allows positional access (get, set, add at index). Main implementations: ArrayList (fast random access), LinkedList (efficient insert/remove at head or in middle).

### Q: Can you use primitive types like int in a List?
No. Generics require reference types. Use List<Integer>, not List<int>. Autoboxing handles conversion when adding/removing.

### Q: What does Arrays.asList() return and can you add or remove elements?
It returns a fixed-size list backed by the array. You cannot add or remove elements; doing so throws UnsupportedOperationException. To get a modifiable list use new ArrayList<>(Arrays.asList(array)).

### Q: What is a Set and how does it differ from List?
Set is a collection that does not allow duplicate elements. It has no positional access (no get(index)). Implementations include HashSet (unordered, O(1) add/contains) and TreeSet (sorted).

### Q: What is a Queue and what are typical operations?
A queue holds elements for processing, typically FIFO. Operations: offer/add (add at tail), poll/remove (remove from head), peek (view head without removing). BlockingQueue blocks when full or empty.

### Q: What is a Deque?
A double-ended queue: insert and remove from both ends. Methods: addFirst, addLast, removeFirst, removeLast, offerFirst, pollLast, etc. ArrayDeque is a common implementation.

### Q: What is a Map and how do you get/put elements?
Map stores key-value pairs; keys must be unique. put(key, value) associates a value; get(key) returns the value or null. keySet(), values(), and entrySet() provide views. HashMap and TreeMap are common implementations.

### Q: What is the difference between HashMap and TreeMap?
HashMap: unordered, O(1) average get/put; keys need hashCode and equals. TreeMap: sorted by natural order or Comparator, O(log n) get/put; keys must be Comparable or you supply a Comparator.
