# Day 22 -- Collections (Part 2) -- Map and Deque

### Q: How do you sort an ArrayList in natural (ascending) order?
Use Collections.sort(list). For comparable types (e.g. Integer, String) elements are sorted from smallest to largest or alphabetically.

### Q: How do you sort a list in a custom order (e.g. descending)?
Use Collections.sort(list, comparator). Pass a Comparator that defines the order; e.g. for descending you return the opposite of the natural comparison.

### Q: What is the Comparator interface used for?
To define custom sort orders. You implement compare(o1, o2): return positive if o1 > o2, negative if o1 < o2, zero if equal. Pass an instance to Collections.sort(list, comparator).

### Q: How do you get an Iterator from a collection and what are its main methods?
Call collection.iterator(). Main methods: hasNext() returns true if there is a next element; next() returns the next element; remove() removes the last element returned by next() (optional operation).

### Q: Does Iterator move backward?
No. Iterator moves only forward (one direction). For backward traversal use ListIterator on a List.

### Q: What extra capabilities does ListIterator have over Iterator?
ListIterator has hasPrevious(), previous(), nextIndex(), previousIndex(), and can set(element) or add(element). It can traverse forward and backward.

### Q: What is the Set interface and how does it differ from List?
Set is a collection that does not allow duplicate elements. It is unordered (except for LinkedHashSet and TreeSet). It models a mathematical set; duplicate adds are ignored.

### Q: What is HashSet and what order does it guarantee?
HashSet stores unique elements using hashing. It does not guarantee any order (insertion order is not preserved); order can appear random based on hash codes.

### Q: What is LinkedHashSet?
LinkedHashSet extends HashSet and maintains insertion order. It stores unique elements and iterates in the order they were added.

### Q: What is TreeSet?
TreeSet implements SortedSet and stores unique elements in sorted order (natural ordering or a custom Comparator). Iteration is in ascending order.

### Q: When would you choose HashSet, LinkedHashSet, or TreeSet?
Use HashSet for uniqueness with no order; LinkedHashSet when you need insertion order; TreeSet when you need sorted order or range operations (headSet, tailSet, subSet).

### Q: Can you call remove() on an Iterator without calling next() first?
No. remove() removes the last element returned by next(). Calling remove() without a prior next() (or calling it twice for the same element) can throw IllegalStateException.

### Q: For String sorting with Collections.sort(list), what order do you get?
Alphabetical (lexicographic) order. Uppercase letters typically sort before lowercase in natural character order; for locale-aware order you would use a Comparator.
