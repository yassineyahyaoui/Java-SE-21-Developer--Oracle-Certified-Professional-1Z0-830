# Module 23 -- Thread Coordination

### Q: How do wait(), notify(), and notifyAll() work?
They are called on the object used as the lock (inside synchronized). wait() releases the lock and blocks until another thread calls notify() (wake one) or notifyAll() (wake all) on that object. The woken thread must reacquire the lock.

### Q: Why use ReentrantLock with Condition instead of synchronized with wait/notify?
ReentrantLock with Condition gives multiple condition variables per lock (e.g. "not full" and "not empty"), explicit lock/unlock, and optional fairness. Use Condition.await() and signal()/signalAll() for signaling.

### Q: Why should you call lock.unlock() in a finally block?
So the lock is always released even if an exception occurs in the try block. Failing to release can cause deadlocks or leave other threads blocked indefinitely.
