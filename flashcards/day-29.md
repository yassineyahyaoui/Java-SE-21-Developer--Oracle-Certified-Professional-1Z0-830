# Day 29 -- Stream API (Part 2): Collectors + Parallel

### Q: How does collect differ from reduce?
collect performs a reduction that builds or mutates a collection (e.g., into a List or Set); reduce returns a single value. Use collect when the result is a collection; use reduce when the result is one value.

### Q: How do you collect stream elements into a List or Set with the collect method?
Use `Collectors.toList()` or `Collectors.toSet()` inside collect, e.g. `stream.filter(...).collect(Collectors.toList())`. The Collectors class provides implementations for useful reduction operations like accumulating into collections.

### Q: What is the filter + collect pattern?
Filter the stream with a predicate, then collect matching elements into a new collection. Example: `list.stream().filter(s -> s.length() > 4).collect(Collectors.toList())`. The source list is unchanged; a new list is created.

### Q: How do you join stream elements into a String with collect?
Use `Collectors.joining(delimiter)` for a simple join, or `Collectors.joining(delimiter, prefix, suffix)` to add prefix and suffix (e.g. `"["` and `"]"`). Joining concatenates input elements in encounter order.

### Q: How do you group stream elements by a criterion?
Use `Collectors.groupingBy(classifier)`. It returns a Map: key = grouping criterion (e.g. length), value = list of elements in that group. Example: `Collectors.groupingBy(String::length)` groups strings by length.

### Q: How do you partition stream elements into two groups by a condition?
Use `Collectors.partitioningBy(predicate)`. It returns a Map with boolean keys: true for elements matching the predicate, false for the rest. Values are lists of elements.

### Q: How do you collect into a specific collection type (e.g. LinkedList)?
Use `Collectors.toCollection(Supplier)`, e.g. `Collectors.toCollection(LinkedList::new)`. The supplier provides the collection instance into which elements are added.

### Q: What is parallel computing in the context of streams?
The work is split across multiple threads (e.g. via Fork/Join); multiple threads process stream elements concurrently. Parallel streams are obtained with `.parallelStream()` on a collection.

### Q: Why might the order of elements differ when using a parallel stream?
Operations run in different threads; completion order is not guaranteed, so output order is not necessarily the same as the source. Use `forEachOrdered` if you need encounter order with parallel streams.

### Q: What is interference in the context of streams, and what can it cause?
Interference is modifying the source (or other data structure) while a stream operation runs. It can cause ConcurrentModificationException or NullPointerException. Do not add or remove elements from the source during stream processing.

### Q: Why is it unsafe to add to an external list inside a parallel stream forEach?
The list is not thread-safe; multiple threads can append at the same time, leading to race conditions and inconsistent results. Use collect (which is thread-safe when the collector supports it) or a thread-safe collection instead.

### Q: What are the conditions for concurrent reduction with collect?
(1) The pipeline uses the collect method. (2) The stream is parallel. (3) The collector has the CONCURRENT characteristic (e.g. `groupingByConcurrent`). (4) Either the stream is unordered or the collector has the UNORDERED characteristic.

### Q: When should you use groupingByConcurrent instead of groupingBy?
Use `groupingByConcurrent` when using a parallel stream and you want a concurrent reduction; it returns a ConcurrentMap and has the CONCURRENT and UNORDERED characteristics. Use `groupingBy` for serial streams or when order matters.

### Q: How do you process elements in encounter order with a parallel stream?
Use `forEachOrdered(consumer)` instead of `forEach(consumer)`. It processes elements in the order defined by the source, but may reduce parallelism benefits.

### Q: Why should lambdas in stream operations be stateless?
Stateless lambdas do not depend on external state and avoid race conditions and non-deterministic results in parallel streams. Stateful lambdas can cause thread-safety issues and should be used with caution.

### Q: When is a stream pipeline actually executed?
Only when a terminal operation is invoked. Intermediate operations use lazy evaluation; the pipeline runs and produces a result when a terminal operation (e.g. collect, forEach, reduce) is called.
