# Module 26 -- Performance and Scalability

### Q: What is thread contention?
When multiple threads compete for the same lock or resource, causing some threads to block. High contention reduces throughput; reduce lock scope or use lock-free structures where possible.

### Q: What is a deadlock and how can you avoid it?
Deadlock occurs when two or more threads wait for each other to release locks (e.g. A holds L1 and waits for L2, B holds L2 and waits for L1). Avoid by always acquiring locks in the same order, or using tryLock with timeout.

### Q: How do you use parallel streams?
Call .parallel() on a stream or use parallelStream() on a collection. Operations run in the common ForkJoinPool. Ensure shared state is not mutated; use thread-safe reduction or avoid shared mutable state.

### Q: When should you use virtual threads vs platform threads?
Use virtual threads for many concurrent tasks that block often (I/O); they are lightweight and the runtime manages them. Use platform threads for CPU-bound work or when you need a small, fixed pool. Do not pool virtual threads.
