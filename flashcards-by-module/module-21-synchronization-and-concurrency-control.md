# Module 21 -- Synchronization and Concurrency Control

### Q: What does the synchronized keyword guarantee when applied to a method?
Only one thread can execute that method on that object at a time. Other threads block until the lock is released. It provides mutual exclusion and visibility for the critical section.

### Q: What does volatile guarantee and what does it NOT guarantee?
Volatile ensures that reads and writes are visible to all threads (no cached stale values). It does NOT guarantee atomicity; e.g. count++ is still not thread-safe with volatile alone.

### Q: When should you use volatile instead of synchronized?
Use volatile for simple flags or single read/write state (e.g. boolean running). Use synchronized when you need atomicity or multi-step updates (e.g. incrementing a counter).

### Q: Why is count++ not thread-safe even with volatile?
count++ is read-modify-write. Volatile only ensures visibility; two threads can both read, increment, and write, losing one update. Use synchronized or AtomicInteger for correct atomic increment.

### Q: What is a critical section?
A part of the code that accesses shared resources and must be executed by only one thread at a time. Protect it with synchronized or a lock to prevent race conditions.
