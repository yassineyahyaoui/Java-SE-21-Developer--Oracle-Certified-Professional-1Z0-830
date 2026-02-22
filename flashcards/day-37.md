# Day 37 -- Virtual Threads + Performance

### Q: What is a thread pool and why use it?
A thread pool is a group of pre-instantiated, reusable threads that execute tasks from a queue. Using one reduces the overhead of creating and destroying threads for each task, improves scalability by limiting active threads, and lets tasks wait in a queue when all threads are busy.

### Q: How does a fixed thread pool behave?
A fixed thread pool has a fixed number of threads. When all are busy, additional tasks wait in an unbounded queue until a thread is free. Suited for steady, predictable workloads and avoids both dynamic thread creation overhead and overprovisioning.

### Q: What thread pool uses ForkJoinPool under the hood and when is it best used?
The work-stealing pool (e.g. `Executors.newWorkStealingPool()`), introduced in Java 8, uses ForkJoinPool. Idle threads steal work from other threads’ queues. It is best for tasks that can be split into subtasks and for CPU-bound or parallel processing of large data sets.

### Q: What is the default size of the common ForkJoinPool used by parallel streams?
By default the common ForkJoinPool size is (number of available processors - 1), so other system work is not starved while parallel streams run.

### Q: How do parallel streams relate to threads and what should you avoid?
Parallel streams use the common ForkJoinPool and split collection elements into chunks processed by multiple threads. Use stateless, non-blocking operations; avoid modifying shared state, which can cause thread-safety issues and non-deterministic order.

### Q: What are the main JVM responsibilities in thread management?
The JVM manages thread lifecycle (NEW, RUNNABLE, BLOCKED/WAITING/TIMED_WAITING, TERMINATED), maps Java threads to OS threads, relies on the OS for context switching, uses thread priorities as hints for the scheduler, and provides synchronization (synchronized, wait/notify). It also runs internal threads (e.g. GC).

### Q: What is the range and default of thread priority in Java?
Thread priority is an integer from 1 (MIN_PRIORITY) to 10 (MAX_PRIORITY); the default is 5 (NORM_PRIORITY). It is only a hint to the scheduler, not a guarantee of order.

### Q: What are daemon threads and when does the JVM exit?
Daemon threads are background threads that do not keep the JVM running. The JVM exits when only daemon threads are left. Set with `setDaemon(true)` before starting the thread; the garbage collector is a daemon thread.

### Q: Describe the thread-per-message concurrency pattern.
In thread-per-message, a new thread is created for every request or task. It is simple and good for lightweight, independent tasks, but can cause high overhead and resource use under heavy load.

### Q: Describe the worker thread (thread pool) concurrency pattern.
A fixed number of worker threads process tasks from a shared queue. Tasks are queued and workers take and run them. Threads are reused, avoiding per-task creation/destruction cost; suitable for high task volume. Tasks may wait when all workers are busy.

### Q: Describe the producer-consumer pattern and typical Java implementation.
Producers add items to a shared buffer; consumers take and process them. A `BlockingQueue` (e.g. `ArrayBlockingQueue`, `LinkedBlockingQueue`) is typically used so producers block when full and consumers block when empty, providing synchronization and decoupling.

### Q: What interfaces/classes are central to thread pool usage in Java?
`Executor` (e.g. `execute(Runnable)`), `ExecutorService` (extends Executor; `submit`, `shutdown`, `shutdownNow`), `Callable` (task that returns a value or throws), `Future` (get result, cancel, isDone), and `Executors` (factory: `newFixedThreadPool`, `newCachedThreadPool`, etc.).

### Q: For CPU-bound vs I/O-bound workloads, how should thread pool size be chosen?
For CPU-bound tasks use a pool size close to the number of CPU cores to avoid thrashing. For I/O-bound tasks use more threads so threads can overlap I/O waits and keep CPUs utilized.

### Q: What does ExecutorService.submit(Callable) return and how do you get the result?
`submit(Callable)` returns a `Future<T>`. You get the result with `future.get()` (blocks until done), check completion with `isDone()`, and cancel with `cancel(boolean)`.
