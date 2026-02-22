# Day 28 -- Stream API (Part 1)

### Q: What is a stream in the Java Stream API?
A stream is a sequence of elements from a data source (e.g. collection, array, file). It does not store data; it operates on data from the source. Once consumed, it cannot be reused.

### Q: Does a stream store data? Can you use it more than once?
No. A stream does not store data and is consumed only once. After a terminal operation runs, the stream is closed; further use throws IllegalStateException.

### Q: How do you create a stream from a collection?
Call `.stream()` on the collection. Example: `List<Integer> numbers = ...; numbers.stream()` or `numbers.stream().forEach(...)` in one chain.

### Q: What is the difference between an intermediate and a terminal operation?
Intermediate operations (e.g. filter, map, sorted) return a Stream and are lazy; they build a pipeline. Terminal operations (e.g. forEach, average, sum) consume the stream and produce a result or side effect; they close the stream.

### Q: What does the filter method do and what does it take as argument?
filter keeps only elements that satisfy a condition. It takes a `Predicate<T>` (e.g. `n -> n % 2 == 0` for even numbers). It is an intermediate operation and returns a Stream.

### Q: What does mapToInt do and when do you use it?
mapToInt maps each element to an int and returns an `IntStream` (not `Stream<Integer>`). Use it when you need int-specific operations like `average()`, `sum()`, `min()`, `max()`.

### Q: How do you get the average of an IntStream and what type does it return?
Call `.average()` on the IntStream. It returns an `OptionalDouble`; use `.getAsDouble()` to get the primitive double value (or handle empty stream with orElse, etc.).

### Q: What terminal reduction operations are available on IntStream for single-value results?
Examples: `sum()` (returns int), `average()` (returns OptionalDouble), `min()` and `max()` (return OptionalInt), and `count()` (returns long). These combine stream elements into one value.

### Q: Why does average() return OptionalDouble instead of double?
Because an empty stream has no defined average; OptionalDouble safely represents presence or absence of a value and avoids a magic number or exception for "no elements."

### Q: What is a stream pipeline?
A sequence of operations on a stream: first create the stream (e.g. from a collection), then chain intermediate operations (filter, map, etc.), and finally a terminal operation that produces the result.

### Q: Can you use a method reference with forEach on a stream?
Yes. If the lambda only calls one method with the stream element as argument, use a method reference: e.g. `stream.forEach(System.out::println)` instead of `stream.forEach(n -> System.out.println(n))`.

### Q: What exception do you get if you use a stream after a terminal operation?
IllegalStateException: "stream has already been operated upon or closed." You must create a new stream from the source if you need to run another pipeline.

### Q: In which package is the Stream interface and since which Java version?
`java.util.stream.Stream`; the Stream API was introduced in Java 8.

### Q: What are reduction operations in the context of streams?
Operations that combine stream elements into a single value (or into a collection). Examples: sum, average, min, max, count; also reduce() and collect() for general-purpose reduction.

### Q: How do filter and map differ in purpose?
filter selects elements that match a predicate (e.g. even numbers). map transforms each element into another value (e.g. add 1, or get string length); both are intermediate operations.
