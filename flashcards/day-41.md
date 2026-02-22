# Day 41 -- Practice Exam + Weak Area Deep Dive

### Q: What is a sealed type and what does the permits clause do?
A sealed class or interface restricts which classes can extend or implement it. The permits clause lists the allowed subclasses or implementors. Each permitted type must be final, sealed, or non-sealed.

### Q: What are the main rules for record components and the record body?
Record components are final and form the canonical constructor parameters. The record body cannot declare additional instance fields; only static fields and compact/canonical constructor logic are allowed. Records are implicitly final.

### Q: How does instanceof pattern matching work in Java 21?
Use `obj instanceof Type name` instead of cast-after-check. If the condition is true, the variable `name` is in scope with that type. No separate cast is needed, and it works in if and switch.

### Q: How do virtual threads differ from platform threads regarding pooling and usage?
Virtual threads should not be pooled; create a new virtual thread per task (e.g. Executors.newVirtualThreadPerTaskExecutor()). They are lightweight and the runtime manages scheduling; pooling is for scarce platform threads.

### Q: In a switch expression, how do guarded patterns work?
Use `case Type t when condition -> value`. The pattern binds the variable; the when clause is an additional boolean expression. The first matching case (pattern + guard true) is chosen. Switch must be exhaustive.

### Q: What makes a switch expression exhaustive?
Every possible value of the selector must be handled by some case (or default). For enums, either list all constants or use default. For sealed types, listing all permitted types or using default satisfies exhaustiveness.

### Q: What are text blocks and how are they delimited?
Text blocks are multi-line string literals using triple quotes """. They start with """ and a newline; content follows; they end with """. Leading whitespace is stripped by the compiler based on the closing """ position.

### Q: Can a record extend another class or be extended?
A record is implicitly final, so it cannot be extended. A record can implement interfaces but cannot extend any class (other than the implicit java.lang.Record).

### Q: Can a non-sealed permitted subclass be extended by any class?
Yes. Non-sealed means the permitted subclass can be extended (or implemented) by any other type without being listed in a permits clause. Only the direct permitted types are restricted by the sealed type.

### Q: How do you create a virtual thread and run a task?
Thread.ofVirtual().start(runnable) or Executors.newVirtualThreadPerTaskExecutor().submit(callable). The executor creates a new virtual thread for each submitted task.

### Q: In pattern matching for switch, what is the order of case matching?
Cases are evaluated in order. The first case whose pattern matches and whose guard (if present) is true is selected. So more specific patterns should appear before more general ones.

### Q: What is the type of a switch expression when different cases return different numeric types?
The result type is the promoted type of all case outcomes (e.g. int and long yield long). All case branches must produce a value (no fall-through) and the types must be compatible.

### Q: When can you use var in a lambda parameter list?
You can use var for all parameters when you want type inference: (var x, var y) -> ... The types are inferred from the target type (e.g. the functional interface). You cannot mix var and explicit types in the same lambda.

### Q: How do records relate to serialization?
Records are serializable if they implement Serializable. The serialization mechanism uses the canonical constructor and component accessors; no special handling is needed for normal record components.

