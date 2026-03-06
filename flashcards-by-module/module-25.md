# Module 25 -- Concurrent Collections

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

### Q: What is Copy on write ArrayList?

Copy on write ArrayList is a thread safe implementation of a list, so each write operation creates a new copy of the underlying array, ensuring no thread conflicts.

### Q: What is Since this?

Since this is an interface, I want to use a class that implements this interface to create an instance.
