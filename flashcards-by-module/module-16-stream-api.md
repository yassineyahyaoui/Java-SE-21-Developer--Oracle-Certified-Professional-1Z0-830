# Module 16 -- Stream API

### Q: What is a stream in the Java Stream API?
A stream is a sequence of elements from a source (collection, array, etc.). It does not store data; it operates on the source. Once consumed by a terminal operation, it cannot be reused.

### Q: What is the difference between intermediate and terminal operations?
Intermediate operations (filter, map, sorted) return a Stream and are lazy; they build a pipeline. Terminal operations (forEach, collect, sum, count) consume the stream and produce a result or side effect; they close the stream.

### Q: What exception do you get if you use a stream after a terminal operation?
IllegalStateException: stream has already been operated upon or closed. Create a new stream from the source for another pipeline.

### Q: What does filter() take as argument and what does it return?
filter takes a Predicate<T> and keeps only elements that satisfy it. It returns a Stream and is intermediate.

### Q: What does map() do?
map transforms each element using a Function<T,R>. It returns a Stream of the new type. Example: stream.map(String::length) gives a stream of lengths.

### Q: What does mapToInt() return and when do you use it?
mapToInt maps to int and returns an IntStream. Use it for int-specific operations: sum(), average(), min(), max().

### Q: What does average() return on an IntStream and why?
OptionalDouble, because an empty stream has no defined average. Use getAsDouble(), orElse(), or ifPresent() to handle the value.

### Q: What are reduction operations?
Operations that combine stream elements into a single value or collection: sum(), count(), min(), max(), reduce(), collect(). They are terminal.

### Q: Why is shared mutable state dangerous with parallel streams?
Parallel streams run in multiple threads. Updating shared mutable state (e.g. a list or counter) without synchronization causes race conditions and incorrect results. Prefer immutable data and proper reduction.
