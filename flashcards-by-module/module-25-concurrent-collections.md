# Module 25 -- Concurrent Collections

### Q: How does ConcurrentHashMap support thread-safe access?
It allows concurrent reads and writes without external synchronization. It uses fine-grained locking so different segments can be accessed concurrently, reducing contention compared to a single lock.

### Q: What is a BlockingQueue?
A queue that blocks when you try to take from an empty queue or put into a full queue (if capacity-bound). Used for producer-consumer patterns. Implementations: ArrayBlockingQueue, LinkedBlockingQueue.

### Q: What is CopyOnWriteArrayList?
A thread-safe List where writes create a new copy of the underlying array. Reads are lock-free and see a consistent snapshot. Good when reads greatly outnumber writes.
