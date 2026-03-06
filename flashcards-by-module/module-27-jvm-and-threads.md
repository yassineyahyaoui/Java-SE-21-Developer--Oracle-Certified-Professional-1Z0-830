# Module 27 -- Java Virtual Machine and Threads

### Q: What is the JVM's role in thread management?
The JVM creates and manages threads; it schedules them (with the OS) and provides thread primitives (synchronization, wait/notify). Each thread has its own stack; objects and class data are shared in the heap.

### Q: What are thread priorities and do they guarantee order?
Threads have a priority (1–10); the JVM uses them as hints for scheduling. They do not guarantee execution order; the scheduler is not required to respect them strictly. Use for hints only, not for correctness.

### Q: What are daemon threads?
Daemon threads do not prevent the JVM from exiting. When all non-daemon threads terminate, the JVM exits and daemon threads are abandoned. Set with setDaemon(true) before start().
