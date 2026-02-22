# Day 25 -- CHECKPOINT: Collections + Exceptions

### Q: What is the String pool and when are literals pooled?
The string pool is a special area in the heap. String literals (e.g. "hello") are interned and reused. Same literal reference equals same object; new String("hello") creates a new object unless interned.

### Q: What is the main difference between StringBuilder and StringBuffer?
StringBuilder is not thread-safe and is preferred when no concurrent access. StringBuffer is thread-safe (synchronized methods). Both are mutable; use for repeated concatenation instead of String.

### Q: Is List.of() mutable? What happens if you try to modify it?
No. List.of() returns an unmodifiable list. Adding, removing, or changing elements throws UnsupportedOperationException. Also nulls are not allowed in List.of().

### Q: When would you choose HashMap vs TreeMap?
Use HashMap when you need fast key lookup and do not care about order. Use TreeMap when you need keys sorted (natural or comparator order). TreeMap has higher cost for insert/lookup due to ordering.

### Q: What is the difference between Comparable and Comparator?
Comparable is implemented by the class itself (compareTo(other)); one natural order. Comparator is external: a separate type with compare(a, b). You can have many comparators for different orderings.

### Q: In try-with-resources, when is close() called and in what order?
close() is called automatically when the try block exits (normally or by exception). Resources are closed in reverse order of declaration.

### Q: What makes an exception checked vs unchecked?
Checked: subclasses of Exception (excluding RuntimeException). Must be handled or declared with throws. Unchecked: RuntimeException and its subclasses and Error; not required to be declared or caught.

### Q: What are the rules for multi-catch (e.g. catch (A | B e))?
Only unrelated exception types can be combined (no one is a subclass of the other). The parameter is effectively final. The same catch block handles both types.

### Q: Does Map extend Collection?
No. Map is not part of the Collection interface hierarchy. It stores key-value pairs; Collection stores single elements.

### Q: In a Queue, in what order are elements removed?
FIFO: first-in, first-out. The element that was added first is removed first (e.g. poll() removes the head).

### Q: How do HashSet and TreeSet differ in ordering and performance?
HashSet: no order, O(1) average for add/contains. TreeSet: sorted order, O(log n) for add/contains. TreeSet requires comparable or comparator for non-natural types.

### Q: If you put the same key twice in a HashMap, what happens?
The second put overwrites the value for that key. The map still has only one entry for that key; get(key) returns the latest value.

### Q: When does the finally block not run?
When the JVM exits (e.g. System.exit()), when the thread is killed, or in some abnormal termination cases. Otherwise it runs after try/catch.

### Q: For custom exceptions, what do you extend for checked vs unchecked?
Extend Exception (or a checked subclass) for checked; extend RuntimeException for unchecked. Call super(message) in your constructor to set the message.

### Q: What do offer() and poll() return when the Queue is full or empty?
offer() returns false when full (capacity-restricted queue). poll() returns null when the queue is empty (no exception).
