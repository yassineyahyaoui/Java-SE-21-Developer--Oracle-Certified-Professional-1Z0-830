# Module 19 -- Overview of Threads

### Q: What is a thread in Java?
A thread is a lightweight unit of execution—a single path of execution within a program. Every Java application has at least one thread (the main thread running main()). Multiple threads allow concurrent execution.

### Q: How do you create a thread by extending Thread?
Create a class that extends Thread and override run() with the code to execute. Instantiate and call start() (not run()) to begin execution in a new thread. Calling run() directly runs it in the current thread with no parallelism.

### Q: How do you create a thread by implementing Runnable?
Create a class that implements Runnable and implement run(). Pass an instance to a Thread: `Thread t = new Thread(new MyRunnable()); t.start();` This separates task logic from thread management.

### Q: What is the difference between a process and a thread?
A process has its own memory space and is independent. Threads live inside a process and share the process's memory. Threads are lighter; multiple threads in one process share resources and can communicate via shared variables.

### Q: What happens if you call run() instead of start() on a Thread?
run() executes in the current thread like any other method; no new thread is created. Always use start() to create a new thread and have the JVM invoke run() in that thread.

### Q: What does Thread.getState() return?
It returns the thread's state as a Thread.State enum: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED. Use it to monitor or debug thread lifecycle.
