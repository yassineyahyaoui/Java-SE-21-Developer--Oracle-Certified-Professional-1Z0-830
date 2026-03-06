# Module 30 -- Tools and Testing

### Q: How can you debug thread issues in Java?
Use thread dumps (jstack or Thread.getAllStackTraces()) to see what each thread is doing and which locks it holds. Use debugger breakpoints and conditional breakpoints. Ensure logging is thread-safe.

### Q: What should you consider when unit testing multithreaded code?
Tests should be deterministic; avoid relying on timing. Use CountDownLatch or similar to synchronize test steps. Test both success and failure paths. Consider using a single-threaded executor for predictable order when testing logic.

### Q: What is profiling and why use it for concurrent apps?
Profiling measures where time is spent (CPU, I/O, locks). For concurrent apps it helps find contention, deadlocks, and bottlenecks. Use profilers (e.g. JFR, VisualVM) to see thread states and lock wait times.
