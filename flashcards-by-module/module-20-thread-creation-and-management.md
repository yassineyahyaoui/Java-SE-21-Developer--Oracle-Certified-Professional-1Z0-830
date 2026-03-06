# Module 20 -- Thread Creation and Management

### Q: What are the main thread states in the thread lifecycle?
NEW (created, start() not called), RUNNABLE (ready or running), BLOCKED (waiting for a monitor lock), WAITING or TIMED_WAITING (waiting for another thread or timeout), TERMINATED (run() finished; thread cannot be restarted).

### Q: How do you get the current thread reference?
Use `Thread.currentThread()` to get the Thread object representing the thread that is currently executing.

### Q: What is a daemon thread and how do you set it?
A daemon thread does not prevent the JVM from exiting; when all non-daemon threads finish, the JVM exits. Set with `thread.setDaemon(true)` before start(). The main thread is non-daemon by default.

### Q: Can you restart a thread after it has terminated?
No. Once a thread's run() method completes, the thread is in TERMINATED state and cannot be restarted. Create a new Thread instance to run the task again.
