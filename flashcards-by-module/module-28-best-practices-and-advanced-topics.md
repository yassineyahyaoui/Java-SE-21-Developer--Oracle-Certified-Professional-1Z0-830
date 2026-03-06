# Module 28 -- Best Practices and Advanced Topics

### Q: What are common concurrency design patterns?
Producer-consumer (BlockingQueue), thread pool (ExecutorService), future/callback (Future, CompletableFuture), and immutable shared data to avoid locking. Prefer high-level APIs over raw threads and locks.

### Q: How should you handle exceptions in worker threads?
Uncaught exceptions in a thread can be lost. Use a try-catch in run(), or set an UncaughtExceptionHandler on the Thread. For ExecutorService, check Future.get() for ExecutionException wrapping the task exception.

### Q: Why prefer immutable objects in concurrent code?
Immutable objects cannot be corrupted by concurrent writes; they are inherently thread-safe. Sharing immutable data avoids synchronization and reduces bugs. Use final fields and no mutators.
