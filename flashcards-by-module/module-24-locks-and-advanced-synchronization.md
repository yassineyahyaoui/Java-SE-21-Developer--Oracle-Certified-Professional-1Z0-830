# Module 24 -- Locks and Advanced Synchronization

### Q: What is ReentrantLock and when do you use it?
ReentrantLock is an explicit lock that supports reentrancy (same thread can acquire multiple times). Use it when you need more control than synchronized: tryLock(), fair ordering, or multiple conditions.

### Q: What is ReentrantReadWriteLock?
A lock that allows multiple readers or one writer. Use when reads are frequent and writes are rare; it can improve concurrency over a single exclusive lock.

### Q: What is a Condition and how do you use it with a lock?
Condition is associated with a Lock; you create it with lock.newCondition(). Use await() to wait, signal() or signalAll() to wake waiters. Always use the same lock when calling await/signal.
