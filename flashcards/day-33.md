# Day 33 -- Java I/O (Part 2)

### Q: How do you read from a .txt file using byte streams?
Use FileInputStream: `InputStream is = new FileInputStream("example.txt");` then read with read() (byte-by-byte, -1 at end) or read(byte[] b). Handle FileNotFoundException and IOException (e.g., with try-catch).

### Q: What is the Writer class and when do you use it?
Writer is an abstract class in java.io for character-based output. Use it when writing text (characters) to files or other sinks; it supports international characters and encoding. Subclasses include FileWriter, BufferedWriter, OutputStreamWriter, CharArrayWriter.

### Q: What is the Reader class and when do you use it?
Reader is an abstract class for character-based input. Use it for reading text as characters (e.g., from .txt files). Subclasses include FileReader, BufferedReader, InputStreamReader, and CharArrayReader.

### Q: How does Reader's read() method work?
The parameterless read() returns the next character as an int (0–65535 for char), or -1 at end of stream. There are also read(char[] cbuf) and read(char[] cbuf, int off, int len). Reader works character-by-character and supports Unicode.

### Q: What is BufferedReader and why use it?
BufferedReader is a Reader subclass that reads text into a buffer, reducing I/O operations. It can wrap another Reader (e.g., FileReader) and provides readLine() for reading a full line. Use it for more efficient character input.

### Q: What is InputStreamReader?
InputStreamReader is a bridge from byte streams to character streams: it reads bytes and decodes them into characters using a charset (or default). Useful when you have an InputStream and want character-based reading with a specific encoding.

### Q: What is CharArrayReader?
CharArrayReader is a Reader that reads from a character array in memory. It takes a char[] (and optional offset and length) and provides character-stream reading from that array.

### Q: How do you distinguish byte streams from character streams?
Byte streams (InputStream/OutputStream): move data in bytes (8 bits); use for binary data or when encoding is not a concern. Character streams (Reader/Writer): move data as characters with encoding (e.g., UTF-8); use for text with international characters.

### Q: Does Reader have an available() method like InputStream?
No. Reader does not have an available() method. To read all text without knowing length in advance, read character-by-character (or into a char array) until read() returns -1 and accumulate into a String or buffer.

### Q: How do you read a specific portion of text (e.g., one word) with Reader?
Use skip(n) to skip to a position, then read(char[] cbuf, int off, int len) to read a fixed number of characters. Alternatively, read the whole content into a String (e.g., by looping with read() and concatenating), then use String methods like indexOf and substring.

### Q: What is FileReader and how do you create one?
FileReader is a Reader subclass for reading character files. Create with `new FileReader("filename.txt")` or a file path. It throws FileNotFoundException; use try-catch or throws.

### Q: What is FileWriter and how do you use it with Writer?
FileWriter is a Writer subclass for writing character files. Use `Writer writer = new FileWriter(path);` then writer.write(int) or writer.write(char[]) or writer.write(String). Close the stream when done.

### Q: Why prefer Reader/Writer for text files over InputStream/OutputStream?
Character streams handle encoding (e.g., UTF-8) and multi-byte characters correctly. Byte streams treat data as raw bytes; for text with international characters, Reader/Writer are the appropriate choice.

### Q: How do you close Reader and Writer properly?
Call close() when done (e.g., in finally or try-with-resources) to release system resources. A closed stream cannot be used again.
