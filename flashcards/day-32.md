# Day 32 -- Java I/O (Part 1)

### Q: What is Java IO and what are streams?
Java IO (input/output) allows programs to read and write data. Operations are primarily stream-based: streams represent sequences of data. Input streams are used for reading; output streams are used for writing. Streams act as a bridge between the program and the data source (e.g., file, keyboard, network).

### Q: What is the difference between byte-based and character-based streams in Java?
Byte-based streams (InputStream/OutputStream and subclasses) transfer data in bytes (8 bits). Character-based streams (Reader/Writer and subclasses) transfer data as characters and support Unicode. Byte streams extend InputStream/OutputStream; character streams extend Reader/Writer.

### Q: What is OutputStream and can you use it directly?
OutputStream is an abstract class in java.io used to transfer data from the program to a sink. It cannot be used directly; you use subclasses such as FileOutputStream, ByteArrayOutputStream, ObjectOutputStream, or PrintStream.

### Q: What are the main write methods of OutputStream?
write(int b) writes one byte; write(byte[] b) writes bytes from the array; write(byte[] b, int off, int len) writes len bytes from b starting at offset off. All can throw IOException (e.g., if the stream is closed).

### Q: What do flush() and close() do on OutputStream?
flush() forces any buffered output bytes to be written to the destination. close() closes the stream and releases system resources; a closed stream cannot perform output and cannot be reopened.

### Q: What is InputStream and how do you use it for file reading?
InputStream is an abstract class for reading data from a source. It cannot be used directly; use a subclass such as FileInputStream for files. FileInputStream constructor takes a file name or path and can throw FileNotFoundException.

### Q: What do the three overloaded read() methods of InputStream do?
read() returns the next byte as an int (0–255), or -1 at end of stream. read(byte[] b) reads bytes into b and returns the number read. read(byte[] b, int off, int len) reads up to len bytes into b starting at off and returns the number read. All throw IOException.

### Q: What do available(), skip(long n), and close() do on InputStream?
available() returns an estimate of bytes that can be read without blocking (do not use to allocate buffers for all data). skip(n) skips and discards n bytes. close() releases resources; a closed stream cannot be reopened.

### Q: What are key subclasses of InputStream?
FileInputStream (files), ByteArrayInputStream (byte arrays), ObjectInputStream (deserialization), and StringBufferInputStream (deprecated). They differ mainly in how they are constructed.

### Q: What are key subclasses of OutputStream?
FileOutputStream (files), ByteArrayOutputStream, ObjectOutputStream (serialization), PrintStream. FileOutputStream is commonly used to write byte data to files.

### Q: Why use try-catch when using InputStream/OutputStream?
read() and write() throw IOException (e.g., I/O error or closed stream). FileInputStream constructor throws FileNotFoundException. Use try-catch or declare throws to handle these.

### Q: How do you read file contents byte-by-byte with InputStream?
Use a loop: call read() (no args), which returns the byte as int 0–255 or -1 at end. Continue while the return value is not -1; cast the int to char or process as needed. Optionally use a byte array with read(byte[] b) for bulk reads.

### Q: In which package are InputStream and OutputStream?
Both are in the java.io package.
