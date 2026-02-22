# Day 39 -- Case Studies + Tools

### Q: In a producer-consumer system, what should the producer do when the shared buffer is full?
The producer must wait until space is available. Use a `while (list.size() == capacity)` loop, then `wait()`. After adding an item, call `notifyAll()` so waiting consumers can proceed.

### Q: In a producer-consumer shared buffer, why use `while` instead of `if` when checking buffer state before wait()?
Using `while` guards against spurious wakeups and ensures the condition is rechecked after being notified. If you used `if`, a single wakeup could let the thread proceed when the buffer is still full or empty.

### Q: In a multithreaded chat server, how do you keep the set of client handlers thread-safe?
Use `Collections.synchronizedSet(new HashSet<>())` so that add/remove/iterate on the set are synchronized. Iterate inside a `synchronized (clientSet)` block when broadcasting to avoid ConcurrentModificationException.

### Q: How does the chat server broadcast a message to all clients except the sender?
Loop over the synchronized set of client handlers; for each client, if it is not the sender, call that client’s `sendMessage(message)`. The broadcast method should take the message and the sender’s ClientHandler so the sender can be skipped.

### Q: What does jstack output when there is a deadlock, and where do you look?
jstack prints a thread dump. Look for a section titled "Found one Java-level deadlock" (often near the end). It lists the threads involved and which locks each holds and is waiting for.

### Q: How do you prevent deadlock when two threads need two locks?
Use a consistent lock order: all threads acquire the same locks in the same order (e.g. always lock1 then lock2). Different orders (thread1: lock1→lock2, thread2: lock2→lock1) can cause circular wait and deadlock.

### Q: When unit testing a ThreadSafeCounter with multiple threads, how do you run many increments concurrently?
Create an ExecutorService (e.g. `Executors.newFixedThreadPool(10)`), submit tasks that call `counter.increment()` (e.g. 1000 times total), then `shutdown()` and `awaitTermination(timeout)`. Use JUnit’s `assertEquals(1000, counter.getCount())` to assert no lost updates.

### Q: Why use ReentrantLock in a thread-safe counter instead of only synchronized?
ReentrantLock gives explicit lock/unlock control and can be used with try-finally to guarantee unlock. For the getter, you must lock before reading and release in finally so the return doesn’t skip the unlock.

### Q: What does Java VisualVM’s Threads tab show?
Thread states (e.g. Running, Waiting, Blocked), thread count, and stack traces. You can take a thread dump from there to inspect locks and detect deadlocks or long waits.

### Q: In VisualVM, how do you find which methods use the most CPU?
Use the Sampler (or Profiler) tab and sample CPU. It shows which methods consume the most CPU time (hotspots), so you can target optimization or lock contention.

### Q: What profiling metrics matter for multithreaded apps?
Thread activity (states, count), CPU hotspots, memory allocation/GC, and lock contention (time spent waiting for locks). High lock contention suggests redesigning synchronization or reducing critical section size.

### Q: In the producer-consumer example, why is the shared buffer class’s produce() method declared with `throws InterruptedException`?
Because it calls `wait()`, which can throw InterruptedException when the thread is interrupted while waiting. The caller (e.g. producer thread’s run()) must handle or declare it.

### Q: In the chat app, why does each connected client get its own thread?
So the server can read from and write to multiple clients at the same time. Each ClientHandler runs in its own thread (started by the server), so one slow client doesn’t block others.

### Q: For the real-time chat client, why is receiving messages done in a separate thread from sending?
So the client can read from the server and read from the console in parallel. One thread runs a loop calling `readLine()` on the server stream; the main thread reads console input and sends it. Otherwise, waiting for a message would block typing.

