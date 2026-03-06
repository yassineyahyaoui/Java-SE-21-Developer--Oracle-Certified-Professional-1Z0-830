# Module 20 -- Thread Creation and Management

### Q: Copy a file using `FileReader`/`FileWriter` (character-based) and `FileInputStream`/`FileOutputStream` (byte-based)?

Copy a file using `FileReader`/`FileWriter` (character-based) and `FileInputStream`/`FileOutputStream` (byte-based)

### Q: What is object serialization (converting an object to a byte stream for storage/transmission)?

Explain object serialization (converting an object to a byte stream for storage/transmission) and deserialization (recreating the object from the byte stream)

### Q: How do you use the `transient` keyword to exclude fields from serialization; state that transient fields get their default values on deserialization (e.g., `0` for `int`)?

Use the `transient` keyword to exclude fields from serialization; state that transient fields get their default values on deserialization (e.g., `0` for `int`)

### Q: What is what a thread is; create threads by extending `Thread` (override `run()`)?

Explain what a thread is; create threads by extending `Thread` (override `run()`) and by implementing `Runnable` (pass to `Thread` constructor, call `start()`)

### Q: Distinguish process vs thread: processes have independent memory, threads share memory within a process; explain multithreading benefits?

Distinguish process vs thread: processes have independent memory, threads share memory within a process; explain multithreading benefits

### Q: What is `start()` (creates a new thread?

Explain `start()` (creates a new thread and calls `run()`) vs calling `run()` directly (runs in current thread, no parallelism); use `Thread.getState()` to monitor thread states (NEW, RUNNABLE)

### Q: What is A thread, on the other hand?

A thread, on the other hand, is a smaller unit within a process.

### Q: What is The browser itself?

The browser itself is a process.

### Q: What is Each thread in Java has its own working memory, which?

Each thread in Java has its own working memory, which is a subset of the main memory.
