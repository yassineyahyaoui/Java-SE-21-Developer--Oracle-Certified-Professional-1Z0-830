# Module 18 -- Java IO (Java Input  Output)

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

### Q: What are key subclasses of InputStream?
FileInputStream (files), ByteArrayInputStream (byte arrays), ObjectInputStream (deserialization). They differ mainly in how they are constructed.

### Q: What are key subclasses of OutputStream?
FileOutputStream (files), ByteArrayOutputStream, ObjectOutputStream (serialization), PrintStream. FileOutputStream is commonly used to write byte data to files.

### Q: What is the Writer class and when do you use it?
Writer is an abstract class in java.io for character-based output. Use it when writing text (characters) to files or other sinks; it supports international characters and encoding. Subclasses include FileWriter, BufferedWriter, OutputStreamWriter, CharArrayWriter.

### Q: What is the Reader class and when do you use it?
Reader is an abstract class for character-based input. Use it for reading text as characters (e.g., from .txt files). Subclasses include FileReader, BufferedReader, InputStreamReader, and CharArrayReader.

### Q: How does Reader's read() method work?
The parameterless read() returns the next character as an int (0–65535 for char), or -1 at end of stream. There are also read(char[] cbuf) and read(char[] cbuf, int off, int len). Reader works character-by-character and supports Unicode.

### Q: What is BufferedReader and why use it?
BufferedReader is a Reader subclass that reads text into a buffer, reducing I/O operations. It can wrap another Reader (e.g., FileReader) and provides readLine() for reading a full line. Use it for more efficient character input.

### Q: Why prefer Reader/Writer for text files over InputStream/OutputStream?
Character streams handle encoding (e.g., UTF-8) and multi-byte characters correctly. Byte streams treat data as raw bytes; for text with international characters, Reader/Writer are the appropriate choice.

### Q: What is object serialization and deserialization?
Serialization converts an object to a byte stream for storage or transmission (e.g., ObjectOutputStream). Deserialization recreates the object from the byte stream (e.g., ObjectInputStream). The class must implement Serializable.

### Q: What does the transient keyword do in serialization?
Fields marked transient are not written to the byte stream during serialization. On deserialization, transient fields get their default values (0, false, null).
