# Module 16 -- Stream API

### Q: What is a?

Define a stream as a sequence of elements from a data source (collection, array, file) that does not store data, only performs operations, and can be consumed only once

### Q: Create streams from collections using `.stream()` and perform operations on list elements via the Stream API?

Create streams from collections using `.stream()` and perform operations on list elements via the Stream API

### Q: How do you use `filter` for conditional element selection and `mapToInt` to convert a stream to an `IntStream`?

Use `filter` for conditional element selection and `mapToInt` to convert a stream to an `IntStream`

### Q: How do you apply terminal reduction operations that combine stream contents into a single value: `average()` (with `getAsDouble()`), `sum`, `min`, `max`, `count`?

Apply terminal reduction operations that combine stream contents into a single value: `average()` (with `getAsDouble()`), `sum`, `min`, `max`, `count`

### Q: Distinguish `collect` from `reduce`: `collect` mutates/builds a collection (e.g., `List` or `Set`) instead of returning a single value?

Distinguish `collect` from `reduce`: `collect` mutates/builds a collection (e.g., `List` or `Set`) instead of returning a single value

### Q: How do you use the `filter` + `collect` pattern to gather matching elements into a new list or set?

Use the `filter` + `collect` pattern to gather matching elements into a new list or set

### Q: What is parallel computing: splitting problems into subproblems solved in separate threads?

Explain parallel computing: splitting problems into subproblems solved in separate threads, then combining results; describe the Fork/Join framework

### Q: What is thread-safety risks with collections: thread interference?

Explain thread-safety risks with collections: thread interference and memory consistency errors; state that synchronization wrappers add safety but introduce contention

### Q: How do you use parallel streams on non-thread-safe collections safely (as long as the collection is not modified during processing)?

Use parallel streams on non-thread-safe collections safely (as long as the collection is not modified during processing)

### Q: What is Stream API?

Stream API is a concept that's kind of entered our lives with Java eight, allowing us to access and process elements that we can store with collections way more easily.

### Q: What is the for each method of the stream class?

Now the for each method of the stream class is a void method, so it's not going to return a stream to us, right?

### Q: What is The map method?

The map method is the stream interface returns a stream consisting of the results of applying the given function to the elements of the stream.

### Q: What is For unordered streams, no stability guarantees are m...?

For unordered streams, no stability guarantees are made because, well, like we just said, this is a stateful intermediate operation.

### Q: What is Check it out I've used the foreach method which?

Check it out I've used the foreach method which is a terminal operation method.

### Q: What is And therefore the stream is now terminated because t...?

And therefore the stream is now terminated because the foreach method is a void method and will not return a stream.

### Q: What is in this example, the identity element is zero and this?

So in this example, the identity element is zero and this is the initial value of the sum of numbers as well as the default value if no members exist in the list of nums.

### Q: What is in this example here, the accumulator function?

So in this example here, the accumulator function is a lambda expression that adds two integer values and returns an integer value.

### Q: What is The initial value?

The initial value is the first parameter zero.

### Q: What is So, for example, if our list?

So, for example, if our list is an empty list, the reduce method would not be able to find an element to sum and will return a null value.

### Q: What is The difference using a starting value is that there?

The difference using a starting value is that there is a value to return if the list is empty.

### Q: What is in this example put in zero so the result will be ze...?

So in this example put in zero so the result will be zero even if it is an empty list.

### Q: What is you may have actually noticed that this?

So you may have actually noticed that this is the reduce method that we use within the scope of reduction operations.

### Q: What is the collectors class?

So the collectors class is an implementation of collector that implements various useful reduction operations, such as accumulating elements into collections, summarizing elements according to various criteria.

### Q: What is Also the groups, that?

Also the groups, that is the value always going to return as a list.

### Q: What is Therefore, we should transfer the result to a map ob...?

Therefore, we should transfer the result to a map object whose key type is integer and whose value type is a list of the type string you follow.

### Q: What is linked list?

Now linked list is a collection class.

### Q: What is the supplier?

So the supplier is a factory function.

### Q: What is The second parameter?

The second parameter is the accumulator.

### Q: What is in this example it will modify the salary collector ...?

So in this example it will modify the salary collector result container by incrementing the count variable by one and adding to the total member variable the value of the stream element, which is an integer representing the salary of a particular member.

### Q: What is And the last parameter?

And the last parameter is the combiner.

### Q: What is as a result, the supplier?

Now as a result, the supplier is a lambda expression or a method reference as opposed to a value like the identity element and the reduce operation.

### Q: What is The second?

The second is a special collector.

### Q: What is one difficulty in implementing parallelism in applic...?

Now, one difficulty in implementing parallelism in applications that use collections is a collections are not thread safe, which means that multiple threads cannot manipulate a collection without introducing thread interference or even memory consistency errors.

### Q: What is The result list?

The result list is an external state and is not thread safe since it works with a parallel stream.
