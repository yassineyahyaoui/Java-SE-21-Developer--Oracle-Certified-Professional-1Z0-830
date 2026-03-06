# Module 26 -- Performance and Scalability

### Q: How do you use `ReentrantLock` with explicit `lock()`/`unlock()` and explain fairness (granting locks in request order); use `ReentrantReadWriteLock` for concurrent read access?

Use `ReentrantLock` with explicit `lock()`/`unlock()` and explain fairness (granting locks in request order); use `ReentrantReadWriteLock` for concurrent read access

### Q: How do you use condition variables with `ReentrantLock` for thread signaling beyond `wait`/`notify`?

Use condition variables with `ReentrantLock` for thread signaling beyond `wait`/`notify`

### Q: What is thread-safe collections?

Explain thread-safe collections and blocking queues for safe concurrent data access

### Q: What is thread?

Define thread contention (multiple threads competing for the same lock) and deadlocks (two or more threads waiting for each other indefinitely)

### Q: What is thread safety through immutability: immutable objects are inherently thread-safe since their state cannot change after construction?

Explain thread safety through immutability: immutable objects are inherently thread-safe since their state cannot change after construction

### Q: What is thread pool optimization: pool of reusable pre-instantiated threads with a task queue?

Explain thread pool optimization: pool of reusable pre-instantiated threads with a task queue, reducing thread creation/destruction overhead for better performance and responsiveness

### Q: How do you use parallel streams (Java 8) with `ForkJoinPool` to split collection processing into chunks across multiple threads on multi-core CPUs?

Use parallel streams (Java 8) with `ForkJoinPool` to split collection processing into chunks across multiple threads on multi-core CPUs

### Q: Describe the JVM's role in thread management and how thread scheduling works?

Describe the JVM's role in thread management and how thread scheduling works

### Q: Set and use thread priorities to influence scheduling order; explain daemon threads (background threads that do not prevent JVM shutdown)?

Set and use thread priorities to influence scheduling order; explain daemon threads (background threads that do not prevent JVM shutdown)

### Q: Describe concurrency design patterns: thread-per-message (new thread per task), worker thread (thread pool pattern), and producer-consumer (coordinating producing and consuming threads)?

Describe concurrency design patterns: thread-per-message (new thread per task), worker thread (thread pool pattern), and producer-consumer (coordinating producing and consuming threads)

### Q: What is the critical section?

Now the critical section is the code that Increments the counter and prints the message.

### Q: What is You may remember immutability?

You may remember immutability is a design principle where the state of an object cannot be modified after it's created.

### Q: What is A thread pool?

A thread pool is a group of pre instantiated threads that are reused to execute tasks.

### Q: What is The first pool?

The first pool is the fixed thread pool.

### Q: What is The first one we got to cover here?

The first one we got to cover here is the executor interface.

### Q: What is the executive interface?

Now the executive interface is the base interface for executing tasks.

### Q: What is Second one?

Second one is the executor service interface.

### Q: What is Next one up?

Next one up is the callable interface, and the callable interface is similar to runnable, but designed for tasks that return a result or can throw a checked exception instead of the run method.

### Q: What is Parallel stream?

So Parallel stream is a feature introduced in Java eight, designed to improve performance by utilizing multiple threads to process a collection of data concurrently.

### Q: What is Say that three times fast, but this?

Say that three times fast, but this is a thread pool designed for parallel processing.

### Q: What is Well, parallel stream happens to be ideal for large ...?

Well, parallel stream happens to be ideal for large data sets and computationally intensive tasks, But avoid parallel streams for small data sets, or when thread safety is a concern, for example, modifying shared variables.
