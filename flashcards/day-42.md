# Day 42 -- Final Review + Exam Readiness

### Q: Why can String comparison with == give false even when the text is the same?
== compares references. Literals and interned strings may share one object in the string pool, but new String(...) or runtime-built strings are different objects. Always use equals() for content comparison.

### Q: When does Integer == return true for two boxed values without using equals()?
Only when the value is in the cache range -128 to 127. Within that range, boxing reuses the same object; outside it, new Integer instances are created and == is false. Use equals() for reliable value comparison.

### Q: What is switch fall-through and how do you avoid it?
Without break (or yield in switch expression), execution falls through to the next case. In switch statements, use break; in switch expressions, each case must produce a value (no fall-through). Fall-through is a common source of bugs.

### Q: Why must a switch expression be exhaustive?
The expression must produce a value for every possible input. Missing cases (e.g. an enum value or a sealed type) cause a compile error. Use default or list all cases to satisfy exhaustiveness.

### Q: Why must a variable used inside a lambda be effectively final?
Lambdas capture variables from the enclosing scope. Allowing mutation would complicate thread safety and scope rules. So the variable must not be reassigned after it is used in the lambda (it can be final or effectively final).

### Q: In try-with-resources, in what order are resources closed?
Resources are closed in the reverse order of their declaration. The last declared resource is closed first, then the second-to-last, and so on. This avoids dependency issues when one resource holds another.

### Q: Why must more specific exception types come before more general ones in catch blocks?
The first matching catch block is used. If IOException is caught before FileNotFoundException, the more specific type would never be reached (compile error: unreachable catch). Order: most specific subclass first, then parent types.

### Q: Can you reuse a stream after a terminal operation has been called?
No. A stream is consumed by one terminal operation. Calling another terminal operation (or iterating again) on the same stream throws IllegalStateException. Create a new stream from the source if you need another pass.

### Q: What is the difference between Period and Duration? Can you mix them?
Period is date-based (years, months, days); Duration is time-based (hours, minutes, seconds, nanos). Do not add a Period to an Instant or use Duration for date-only math; use Period with LocalDate and Duration with Instant/LocalTime.

### Q: Why is shared mutable state dangerous with parallel streams?
Parallel streams run in multiple threads. Updating shared mutable state (e.g. a list or counter) without synchronization causes race conditions and incorrect results. Use thread-safe structures or avoid shared mutation; prefer immutable data and proper reduction.

### Q: What must every permitted subclass of a sealed class or interface declare?
It must be explicitly declared as final, sealed, or non-sealed. Omitting this is a compile error. If sealed, it must have its own permits clause listing its direct subclasses.

### Q: Can a record declare additional instance fields or be mutable?
No. All record components are implicitly final. You cannot add instance fields in the body. You can add static fields and methods. Records are designed as immutable data carriers.

### Q: How should you use virtual threads in terms of pooling and task assignment?
Do not pool virtual threads. Create one virtual thread per task (e.g. via Executors.newVirtualThreadPerTaskExecutor()). Pooling is for platform threads; virtual threads are cheap and meant to be created per unit of work.

