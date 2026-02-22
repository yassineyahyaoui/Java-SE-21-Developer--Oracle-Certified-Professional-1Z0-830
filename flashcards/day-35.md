# Day 35 -- Concurrency Core

### Q: What is synchronization in Java multithreading?
Synchronization controls access to shared resources so that only one thread executes a critical section at a time. Use the `synchronized` keyword on methods or blocks to prevent thread interference and race conditions.

### Q: What does the synchronized keyword guarantee when applied to a method?
Only one thread can execute that method on that object at any given time. Other threads block until the lock is released. It provides both visibility and atomicity for the critical section.

### Q: What does volatile guarantee, and what does it NOT guarantee?
Volatile ensures that reads and writes to the variable are visible to all threads (no caching of stale values). It does NOT guarantee atomicity; e.g. it does not make operations like `count++` thread-safe.

### Q: When should you use volatile instead of synchronized?
Use volatile for simple flags or state that is only read/written (e.g. a boolean `running` to stop a thread). Use synchronized when you need atomicity or multi-step updates (e.g. incrementing a counter).

### Q: Why can count++ be wrong with multiple threads even with volatile?
Because `count++` is read-modify-write (read, increment, write). Volatile only ensures visibility; two threads can still both read the same value, increment, and write, so one update is lost. Use synchronized or AtomicInteger for correctness.

### Q: What is the Executor framework and why use it?
The Executor framework decouples task submission from execution. Use `ExecutorService` (e.g. `Executors.newFixedThreadPool(n)`) to manage thread pools instead of creating threads manually, improving efficiency and control.

### Q: What is ScheduledExecutorService used for?
ScheduledExecutorService schedules tasks to run after a delay or at fixed intervals. Use `schedule()`, `scheduleAtFixedRate()`, or `scheduleWithFixedDelay()` for periodic or delayed execution.

### Q: How does ConcurrentHashMap support thread-safe access?
ConcurrentHashMap allows multiple threads to read and write safely without external synchronization. It uses fine-grained locking (e.g. segment-level) so different parts can be accessed concurrently, reducing contention.

### Q: How does Callable differ from Runnable?
Callable can return a result and throw checked exceptions; Runnable returns void and cannot throw checked exceptions. Use Callable when you need a result from a background task.

### Q: What does Future.get() do?
Future.get() blocks the calling thread until the asynchronous computation completes, then returns the result. It can throw ExecutionException (wrapping the task exception) or InterruptedException.

### Q: What are AtomicInteger and similar atomic variables used for?
They provide lock-free, thread-safe operations on a single variable (e.g. increment, add). Use `incrementAndGet()`, `getAndAdd()`, etc. when you need atomic updates without explicit locks or synchronized blocks.

### Q: What is a Semaphore and how is it used?
A Semaphore controls how many threads can access a resource at once via permits. Threads acquire a permit before using the resource and release it after; if no permit is available, the thread blocks. Useful for limiting concurrency (e.g. DB connections).

### Q: How do wait(), notify(), and notifyAll() work for inter-thread communication?
They are called on the same object used as the lock. wait() releases the lock and blocks until another thread calls notify() (wake one) or notifyAll() (wake all) on that object. The woken thread must reacquire the lock before continuing.

### Q: Why use ReentrantLock with Condition instead of synchronized with wait/notify?
ReentrantLock with Condition gives multiple condition variables per lock (e.g. "not full" and "not empty"), explicit lock/unlock, and optional fairness. Use Condition.await() and Condition.signal() / signalAll() for signaling; always call unlock() in a finally block.

### Q: What is a critical section?
A critical section is a part of the code that accesses shared resources and must be executed by only one thread at a time. Protecting it with synchronized or a lock prevents race conditions.

### Q: Why should you call lock.unlock() in a finally block when using ReentrantLock?
So the lock is always released even if an exception occurs inside the try block. Failing to release the lock can cause deadlocks or leave other threads blocked indefinitely.
