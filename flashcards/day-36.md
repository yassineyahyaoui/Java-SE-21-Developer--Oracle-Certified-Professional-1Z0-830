# Day 36 -- Concurrency Advanced

### Q: How do you use ReentrantLock for synchronization?
Create a `ReentrantLock`, call `lock()` before the critical section, perform the work in a try block, and call `unlock()` in a finally block so the lock is always released. Only one thread holds the lock at a time.

### Q: What is fairness in ReentrantLock and how do you enable it?
Fairness means threads acquire the lock in the order they requested it (FIFO). Use `new ReentrantLock(true)` to create a fair lock. Without fairness, the JVM may let threads acquire out of order for performance.

### Q: What is ReentrantReadWriteLock and when is it useful?
It separates read and write locks: multiple threads can hold the read lock concurrently, but only one thread can hold the write lock (and no readers). Use it when reads are frequent and writes are rare for better concurrency than a single mutex.

### Q: With ReentrantReadWriteLock, can a thread hold both read and write lock?
Yes. The same thread can acquire the read lock and later the write lock (reentrancy). The write lock is exclusive with other writers and readers; the read lock is shared among readers only.

### Q: What are Condition variables and how do they relate to ReentrantLock?
Condition variables let threads wait and be signaled under specific conditions. Create with `lock.newCondition()`. Use `await()`, `signal()`, and `signalAll()` instead of Object's wait/notify; they work with the same ReentrantLock and allow multiple conditions (e.g. "notFull", "notEmpty") per lock.

### Q: Name some thread-safe collections in java.util.concurrent.
ConcurrentHashMap, CopyOnWriteArrayList, ConcurrentLinkedQueue, ConcurrentSkipListMap, ConcurrentSkipListSet, LinkedBlockingQueue, ArrayBlockingQueue, PriorityBlockingQueue. They are designed for concurrent access without external synchronization.

### Q: When is CopyOnWriteArrayList a good choice?
When reads greatly outnumber writes. Each write creates a new copy of the underlying array, so writes are costly but reads are lock-free and fast. Avoid for frequently updated shared lists.

### Q: What are blocking queues and how do put() and take() behave?
Blocking queues (e.g. LinkedBlockingQueue, ArrayBlockingQueue) are thread-safe queues that block: put() blocks if the queue is full, take() blocks if the queue is empty. They are ideal for producer-consumer patterns.

### Q: What is thread contention?
Thread contention occurs when multiple threads compete for the same resource (e.g. a lock or variable). Threads wait for each other, causing delays and reduced throughput. Reduce it by minimizing lock scope and using concurrent data structures.

### Q: What is a deadlock and what typically causes it?
A deadlock is when two or more threads are blocked, each waiting for a resource held by another. A classic cause is circular lock ordering: Thread A holds lock1 and waits for lock2, Thread B holds lock2 and waits for lock1.

### Q: How can you avoid deadlocks?
Use consistent lock ordering (all threads acquire locks in the same order), avoid nested locks when possible, and use tryLock with a timeout so threads do not wait indefinitely.

### Q: How does immutability help with thread safety?
Immutable objects cannot be changed after creation, so no synchronization is needed when sharing them. Multiple threads can read the same immutable object safely; there are no race conditions on its state.

### Q: What are the main rules to make a class immutable in Java?
Make the class final; make all fields private and final; do not provide setter methods; ensure mutable fields are not exposed (deep copy or defensive copy); provide only getters or methods that return new instances for "updates."

### Q: Why prefer immutable objects in multithreaded code when possible?
They eliminate race conditions, keep state consistent, simplify reasoning and debugging, and avoid synchronization overhead. Shared mutable state requires locks or other coordination; immutable shared state is safe by design.

### Q: What is a race condition?
A race condition occurs when the result of a computation depends on the timing or order of thread execution. Multiple threads access shared data concurrently and at least one modifies it, leading to unpredictable or incorrect results.
