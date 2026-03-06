# Module 22 -- High-level Concurrency APIs

### Q: What is synchronization: controlling access to shared resources so only one thread executes a critical section at a time; use the `synchronized` keyword on methods (counter example demonstrating thread interference?

Explain synchronization: controlling access to shared resources so only one thread executes a critical section at a time; use the `synchronized` keyword on methods (counter example demonstrating thread interference and its fix)

### Q: What is the `volatile` keyword: ensures a variable is immediately visible to all threads but does not guarantee atomicity?

Explain the `volatile` keyword: ensures a variable is immediately visible to all threads but does not guarantee atomicity

### Q: How do you use the Executor framework: create thread pools with `Executors.newFixedThreadPool()` and schedule tasks with `ScheduledExecutorService` (`newScheduledThreadPool`, delays, fixed intervals)?

Use the Executor framework: create thread pools with `Executors.newFixedThreadPool()` and schedule tasks with `ScheduledExecutorService` (`newScheduledThreadPool`, delays, fixed intervals)

### Q: How do you use `ConcurrentHashMap` for thread-safe data handling without manual synchronization?

Use `ConcurrentHashMap` for thread-safe data handling without manual synchronization

### Q: How do you use `Callable` (returns a result, unlike `Runnable`) with `Future.get()` (blocks until result ready); use `AtomicInteger` for lock-free thread-safe counter operations?

Use `Callable` (returns a result, unlike `Runnable`) with `Future.get()` (blocks until result ready); use `AtomicInteger` for lock-free thread-safe counter operations

### Q: Coordinate threads with `Semaphore` (permits controlling how many threads access a resource); use `wait()`, `notify()`, `notifyAll()` for inter-thread communication; use `ReentrantLock` with `Condition` for fine-grained control?

Coordinate threads with `Semaphore` (permits controlling how many threads access a resource); use `wait()`, `notify()`, `notifyAll()` for inter-thread communication; use `ReentrantLock` with `Condition` for fine-grained control

### Q: What is Callable?

Callable is an interface in Java, much like runnable, but with one major difference it can return a result or throw a checked exception.

### Q: What is And this?

And this is the interface that we're going to use to manage thread pools.

### Q: What is Runnable?

Runnable is an interface that defines a single method run.

### Q: What is here the callable?

So here the callable is a lambda expression that prints the thread name, simulates some work with a thread dot sleep and put 2000 and returns a result.
