# Day 21 -- Collections (Part 1) -- List and Set

### Q: What is the root of the Java Collections Framework hierarchy?
The Collection interface is the root. Core sub-interfaces include List, Set, Queue, and Deque. Map is separate (not a Collection).

### Q: How does Collection differ from an array?
Arrays have fixed size; collections (e.g. ArrayList) can grow and shrink. Collections provide methods to add, remove, and access elements; arrays do not change size after creation.

### Q: What is the List interface and what are its main properties?
List is an ordered collection that allows duplicate elements. It allows positional access (by index) and insertion at specific positions. It extends Collection.

### Q: What are the two general-purpose List implementations and when to use which?
ArrayList and LinkedList. ArrayList is usually better for most uses (fast random access by index). LinkedList offers better performance for frequent insertions/removals at the beginning or in the middle.

### Q: How do you declare and instantiate a List (e.g. of String)?
List<String> list = new ArrayList<>(); You need a concrete class (e.g. ArrayList) because List is an interface. Use wrapper types (Integer, Double) not primitives in generics.

### Q: Can you use primitive types like int in a List?
No. Collections use generics with reference types only. Use wrapper classes: List<Integer>, not List<int>.

### Q: What does add(element) do? What about add(index, element)?
add(element) appends to the end. add(index, element) inserts at that index and shifts existing elements to the right.

### Q: How do you get, change, and remove elements in a List?
get(index) returns the element; set(index, newValue) replaces it; remove(index) or remove(object) removes an element. size() returns the number of elements.

### Q: What do contains(), isEmpty(), and clear() do?
contains(obj) returns true if the list contains the element; isEmpty() returns true if size is 0; clear() removes all elements.

### Q: How do you convert a List to an array?
Use toArray(): with no argument it returns Object[]; with an array argument, e.g. list.toArray(new String[0]) or list.toArray(new String[list.size()]), it returns a typed array.

### Q: How do you convert an array to a List?
Arrays.asList(array) returns a fixed-size list backed by the array (cannot add/remove; changes to list or array affect each other). To get a modifiable list use new ArrayList<>(Arrays.asList(array)) or Collections.addAll(list, array).

### Q: Can you add elements to a list created with Arrays.asList()?
No. The list returned by Arrays.asList() is fixed-size and backed by the array. Adding or removing throws UnsupportedOperationException.

### Q: What does ArrayList equals() compare?
It compares elements in order. Two lists are equal if they have the same size and corresponding elements are equal (by their equals()). Type of the list (e.g. List<String> vs List<Object>) does not affect equality of contents.
