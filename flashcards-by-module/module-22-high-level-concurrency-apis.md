# Module 22 -- High-level Concurrency APIs

### Q: What is the Executor framework and why use it?
It decouples task submission from execution. Use ExecutorService (e.g. Executors.newFixedThreadPool(n)) to manage thread pools instead of creating threads manually, improving efficiency and control.

### Q: How does Callable differ from Runnable?
Callable returns a result and can throw checked exceptions; Runnable returns void and cannot throw checked exceptions. Use Callable when you need a result from a background task.

### Q: What does Future.get() do?
It blocks the calling thread until the asynchronous computation completes, then returns the result. It can throw ExecutionException (wrapping the task exception) or InterruptedException.

### Q: What is ScheduledExecutorService used for?
Scheduling tasks to run after a delay or at fixed intervals. Use schedule(), scheduleAtFixedRate(), or scheduleWithFixedDelay() for delayed or periodic execution.

### Q: What are AtomicInteger and similar atomic variables used for?
Lock-free, thread-safe operations on a single variable (increment, add, compare-and-set). Use incrementAndGet(), getAndAdd(), etc. when you need atomic updates without explicit locks.

### Q: How do you create and use virtual threads (Java 21)?
Thread.ofVirtual().start(runnable) or Executors.newVirtualThreadPerTaskExecutor().submit(callable). Virtual threads are lightweight; create one per task rather than pooling. Do not pool virtual threads.
