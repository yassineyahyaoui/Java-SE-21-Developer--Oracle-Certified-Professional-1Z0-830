# Day 34 -- Java I/O (Part 3) + Thread Basics

### Q: How do you copy a file using FileReader and FileWriter?
Open a FileReader on the source and a FileWriter on the destination. In a loop, read with reader.read() (returns int, -1 at end); while not -1, write with writer.write(characterRead). Close both streams when done.

### Q: How do you copy a file using FileInputStream and FileOutputStream?
Open FileInputStream for the source and FileOutputStream for the destination. Read bytes (e.g., with read(byte[] buffer)) and write them with write(byte[], 0, bytesRead) until read returns -1. Close both streams.

### Q: What is object serialization in Java?
Serialization is converting a Java object into a byte stream so it can be stored (e.g., in a file) or transmitted (e.g., over a network). The byte stream is platform-independent and can be used to reconstruct the object later via deserialization.

### Q: What is deserialization?
Deserialization is the reverse of serialization: converting a byte stream back into a Java object. In Java it is done with ObjectInputStream (e.g., wrapping a FileInputStream). The class must be serializable and have a public no-arg constructor; the constructor is not called during deserialization.

### Q: How do you make a class serializable?
The class must implement the Serializable interface from java.io. Serializable is a marker interface (no methods); it only marks the class as eligible for serialization. Use ObjectOutputStream to write objects and ObjectInputStream to read them.

### Q: What is the transient keyword and what does it do during serialization?
transient marks a field so it is excluded from serialization. When the object is deserialized, that field gets its default value (e.g., 0 for int/long, false for boolean, null for reference types).

### Q: Why use transient?
Two main reasons: (1) You do not want certain data serialized (e.g., passwords, IDs) for security or clarity. (2) A field's type is not Serializable; marking it transient avoids NotSerializableException while the rest of the object is serialized.

### Q: What is a thread in Java?
A thread is a lightweight unit of execution—a single path of execution within a program. Every Java application has at least one thread (the main thread) that runs main(). Multiple threads allow concurrent execution and better responsiveness.

### Q: How do you create a thread by extending Thread?
Create a class that extends Thread and override run() with the code to execute. Instantiate the class and call start() (not run()) to begin execution in a new thread. Example: `class MyThread extends Thread { @Override public void run() { ... } }` then `new MyThread().start();`

### Q: How do you create a thread by implementing Runnable?
Create a class that implements Runnable and implement run(). Pass an instance to a Thread: `Thread t = new Thread(new MyRunnable()); t.start();` This separates task logic from thread management and allows the class to extend another class.

### Q: What is the difference between a process and a thread?
A process is an independent program with its own memory space. Threads are units within a process and share the process's memory. Processes are isolated; threads share memory and resources within the same process, making communication between threads easier.

### Q: What happens if you call run() instead of start() on a Thread?
Calling run() directly runs the method in the current thread like any other method; no new thread is created and there is no parallelism. Always use start() to create a new thread and have the JVM invoke run() in that thread.

### Q: What does Thread.getState() do?
getState() returns the current state of the thread as a Thread.State enum (e.g., NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED). Use it to monitor or debug thread lifecycle.

### Q: What are the main thread states in the thread lifecycle?
NEW (created, start() not called), RUNNABLE (ready or running after start()), BLOCKED (waiting for a monitor lock), WAITING or TIMED_WAITING (waiting for another thread or for a timeout), TERMINATED (run() finished; thread cannot be restarted).

### Q: Which classes are used for serialization and deserialization?
ObjectOutputStream (wraps an OutputStream such as FileOutputStream) for serialization—write objects with writeObject(). ObjectInputStream (wraps an InputStream such as FileInputStream) for deserialization—read with readObject(), which can throw ClassNotFoundException.
