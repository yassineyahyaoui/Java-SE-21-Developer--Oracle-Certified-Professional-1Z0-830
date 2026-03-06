# Module 18 -- Java IO (Java Input  Output)

### Q: What is Java IO fundamentals: stream-based input/output for file operations (create?

Explain Java IO fundamentals: stream-based input/output for file operations (create, write, read, delete); input streams for reading data, output streams for writing data

### Q: How do you use the `OutputStream` abstract class and its subclass `FileOutputStream` to write byte data to files?

Use the `OutputStream` abstract class and its subclass `FileOutputStream` to write byte data to files

### Q: How do you use the `InputStream` abstract class and its subclass `FileInputStream` to read byte data from files; list key subclasses (`ByteArrayInputStream`, `ObjectInputStream`)?

Use the `InputStream` abstract class and its subclass `FileInputStream` to read byte data from files; list key subclasses (`ByteArrayInputStream`, `ObjectInputStream`)

### Q: Distinguish between byte-based streams (`InputStream`/`OutputStream`) that transfer data in bytes and character-based streams introduced later?

Distinguish between byte-based streams (`InputStream`/`OutputStream`) that transfer data in bytes and character-based streams introduced later

### Q: Read from `.txt` files hands-on using `FileInputStream` and print contents to the console?

Read from `.txt` files hands-on using `FileInputStream` and print contents to the console

### Q: What is the `Writer` class: character-based output (vs byte-based)?

Explain the `Writer` class: character-based output (vs byte-based), supports international characters (introduced in Java 1.1)

### Q: What is the `Reader` class: character-based input?

Explain the `Reader` class: character-based input, abstract with subclasses `BufferedReader`, `InputStreamReader`, `CharArrayReader`; use `read()` method overloads

### Q: Distinguish between byte streams (`InputStream`/`OutputStream` for raw bytes) and character streams (`Reader`/`Writer` for text with character encoding)?

Distinguish between byte streams (`InputStream`/`OutputStream` for raw bytes) and character streams (`Reader`/`Writer` for text with character encoding)

### Q: Copy a file using `FileReader`/`FileWriter` (character-based) and `FileInputStream`/`FileOutputStream` (byte-based)?

Copy a file using `FileReader`/`FileWriter` (character-based) and `FileInputStream`/`FileOutputStream` (byte-based)

### Q: What is object serialization (converting an object to a byte stream for storage/transmission)?

Explain object serialization (converting an object to a byte stream for storage/transmission) and deserialization (recreating the object from the byte stream)

### Q: How do you use the `transient` keyword to exclude fields from serialization; state that transient fields get their default values on deserialization (e.g., `0` for `int`)?

Use the `transient` keyword to exclude fields from serialization; state that transient fields get their default values on deserialization (e.g., `0` for `int`)

### Q: What is what a thread is; create threads by extending `Thread` (override `run()`)?

Explain what a thread is; create threads by extending `Thread` (override `run()`) and by implementing `Runnable` (pass to `Thread` constructor, call `start()`)

### Q: Distinguish process vs thread: processes have independent memory, threads share memory within a process; explain multithreading benefits?

Distinguish process vs thread: processes have independent memory, threads share memory within a process; explain multithreading benefits

### Q: What is `start()` (creates a new thread?

Explain `start()` (creates a new thread and calls `run()`) vs calling `run()` directly (runs in current thread, no parallelism); use `Thread.getState()` to monitor thread states (NEW, RUNNABLE)

### Q: What is then what?

So then what is the output stream class.

### Q: What is the method of this class used to write data?

So the method of this class used to write data is the right method.

### Q: What is The first method?

The first method is the right method.

### Q: What is the last one?

Now the last one is the three parameters write method.

### Q: What is The first parameter?

The first parameter is the byte array, the type of the second and the third parameters are both int Udur okay.

### Q: What is The second parameter?

The second parameter is the start offset in the data, and the third parameter is the number of bytes to write.

### Q: What is Element B off?

Element B off is the first byte written, and b off plus Len minus one is the last byte written by this operation.

### Q: What is the general contract of flush is that calling it?

Now the general contract of flush is that calling it is an indication that if any bites previously written have been buffered by the implementation of the output stream, such bytes should immediately be written to their intended destination you follow.

### Q: What is if the intended destination of the stream?

So if the intended destination of the stream is an abstraction provided by the underlying operating system, for example, a file, then flushing the stream guarantees that only bytes previously written to the stream are passed to the operating system for writing.

### Q: What is the last method to look at?

So the last method to look at is the close method.

### Q: What is Then with the help of the Fileoutputstream class which?

Then with the help of the Fileoutputstream class which is the subclass of the output stream class, we'll create a file in the file directory of our computer, the name and the extension of which we're going to specify.

### Q: What is And here you can see the output stream class?

And here you can see the output stream class is an abstract class.

### Q: What is the example right?

So the example right is the file name and the dot txt is its extension.

### Q: What is you got to notice that the index number of p, which?

Now you got to notice that the index number of p, which is the first letter of the word programming, is five.

### Q: What is the method of this class used to read data?

So the method of this class used to read data is the read method.

### Q: What is The first one?

The first one is the parameter list read method.

### Q: What is Otherwise there?

Otherwise there is an attempt to read at least one byte, and if no byte is available because the stream is at the end of the file, the value minus one is returned.

### Q: What is Otherwise, at least one byte is read and stored in t...?

Otherwise, at least one byte is read and stored in the B, and then the last one is the three parameters.

### Q: What is The type of the first parameter?

The type of the first parameter is the byte array.

### Q: What is Otherwise, there?

Otherwise, there is an attempt to read at least one byte.

### Q: What is The second method?

The second method is the available method.
