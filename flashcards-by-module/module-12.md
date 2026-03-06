# Module 12 -- Collections

### Q: Describe the Java Collections Framework hierarchy: `Collection` interface with `Set`, `List`, `Queue`, `Deque` children; distinguish interfaces from implementing classes?

Describe the Java Collections Framework hierarchy: `Collection` interface with `Set`, `List`, `Queue`, `Deque` children; distinguish interfaces from implementing classes

### Q: What is the `List` interface: ordered?

Explain the `List` interface: ordered, allows duplicates; compare `ArrayList` (fast random access) vs `LinkedList` (fast insert/remove at ends); use type parameters with generics

### Q: Create an `ArrayList`, add elements with `add()`, and perform common List operations (get, set, remove, size, contains)?

Create an `ArrayList`, add elements with `add()`, and perform common List operations (get, set, remove, size, contains)

### Q: Convert between lists and arrays using `toArray()` (no-arg and with array parameter), `Arrays.asList()`, and `Collections.addAll()`?

Convert between lists and arrays using `toArray()` (no-arg and with array parameter), `Arrays.asList()`, and `Collections.addAll()`

### Q: Sort an `ArrayList` using `Collections.sort()` for natural (ascending/alphabetical) order?

Sort an `ArrayList` using `Collections.sort()` for natural (ascending/alphabetical) order

### Q: How do you use the `Comparator` interface to define custom sort orders (e.g., descending) and pass it to the overloaded `Collections.sort(list, comparator)`?

Use the `Comparator` interface to define custom sort orders (e.g., descending) and pass it to the overloaded `Collections.sort(list, comparator)`

### Q: Search elements in a sorted `ArrayList` and use `Iterator` / `ListIterator` to traverse a collection one element at a time with `hasNext()`, `next()`, and `remove()`?

Search elements in a sorted `ArrayList` and use `Iterator` / `ListIterator` to traverse a collection one element at a time with `hasNext()`, `next()`, and `remove()`

### Q: What is the `Set` interface: unordered?

Explain the `Set` interface: unordered, no duplicates; distinguish `HashSet` (hashing, no order, allows one `null`), `LinkedHashSet` (insertion order), and `TreeSet` (sorted order)

### Q: Create and use `HashSet`, `LinkedHashSet`, and `TreeSet` in practice and predict element ordering for each?

Create and use `HashSet`, `LinkedHashSet`, and `TreeSet` in practice and predict element ordering for each

### Q: What is the `Queue` interface (FIFO)?

Explain the `Queue` interface (FIFO) and create queues with `PriorityQueue` and `LinkedList`; use `offer()`, `poll()`, and `peek()`

### Q: What is the `Deque` interface (double-ended queue?

Explain the `Deque` interface (double-ended queue, supports both FIFO and LIFO) and use `ArrayDeque` as both a stack (`push`/`pop`/`peek`) and a queue (`offer`/`poll`/`peek`)

### Q: How do you use the `Map` interface for key-value pairs; distinguish `HashMap` (no order), `LinkedHashMap` (insertion order), and `TreeMap` (sorted by key); state that `Map` is not part of the `Collection` interface?

Use the `Map` interface for key-value pairs; distinguish `HashMap` (no order), `LinkedHashMap` (insertion order), and `TreeMap` (sorted by key); state that `Map` is not part of the `Collection` interface

### Q: Create `HashMap` instances, add entries with `put()`, retrieve with `get()`, and explain that duplicate keys are not allowed (value is overwritten)?

Create `HashMap` instances, add entries with `put()`, retrieve with `get()`, and explain that duplicate keys are not allowed (value is overwritten)

### Q: What is At the top of the hierarchy?

At the top of the hierarchy is the collection interface itself.

### Q: What is The collection interface?

The collection interface is the least common denominator that all collections implement.

### Q: What is Sometimes it's called a sequence, but you got to rem...?

Sometimes it's called a sequence, but you got to remember that list is an ordered collection, so lists can actually contain duplicate elements.

### Q: What is The point is, whatever the ordering that's being use...?

The point is, whatever the ordering that's being used, the head of the queue is the element that would be removed by a call to remove or poll.

### Q: What is Since list?

Since list is an interface, we cannot create an object directly from the list interface.

### Q: What is Finally there?

Finally there is a constructor parenthesis.

### Q: What is And of course if there?

And of course if there is an element already in the index it shifts it over to the right.

### Q: What is The first?

The first is the index number of the element to be changed.

### Q: What is And the second one?

And the second one is the new value of the element.

### Q: What is And as you can see, the list?

And as you can see, the list is an interface and it is under the Java.util package.

### Q: What is And that's because the collection interface?

And that's because the collection interface is the root interface.

### Q: What is the ArrayList?

So the ArrayList is a subclass of the list and collections.

### Q: What is if you move the cursor over the list it says list?

So if you move the cursor over the list it says list is a raw type.

### Q: What is The second parameter?

The second parameter is the element that I want to add.

### Q: What is Okay, so there?

Okay, so there is the cat element at index one.

### Q: What is the first one?

So the first one is the name of the list and the other one is the name of the array.

### Q: What is it's thanks to this get method we can actually get t...?

Now it's thanks to this get method we can actually get the elements of a list, which is the specific index.

### Q: What is my friends you can see the output?

So my friends you can see the output is the same.

### Q: What is yeah the output?

So yeah the output is the same.

### Q: What is There you see the output?

There you see the output is the same.

### Q: What is Yeah there the output?

Yeah there the output is the same.

### Q: What is the cars list and the second parameter?

So the cars list and the second parameter is the array.
