# Module 29 -- Case Studies and Practical Scenarios

### Q: What is a typical producer-consumer setup in Java?
Use a BlockingQueue. Producer(s) call put() to add items; consumer(s) call take() to remove. The queue blocks when full (put) or empty (take), coordinating threads without explicit wait/notify.

### Q: How do you design a thread-safe cache?
Use ConcurrentHashMap for the cache map. For compute-if-absent semantics use computeIfAbsent() or putIfAbsent(). Consider expiration (e.g. time-based) and size limits. Avoid caching mutable objects that are changed after insertion or ensure they are thread-safe/immutable.

### Q: What should you avoid when writing multithreaded code?
Avoid shared mutable state without synchronization; lock ordering that can cause deadlock; blocking inside a lock for long periods; and assuming thread priorities or scheduling order. Prefer high-level concurrency APIs and immutable data.
