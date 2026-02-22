# Day 20 -- Strings (Part 2) + Text Blocks

### Q: What is StringBuffer and how is it different from String?
StringBuffer is a class used to create mutable (modifiable) character sequences. Unlike String, the length and content can be changed through method calls; it is stored in the heap.

### Q: How do you add to a StringBuffer?
Use the append() method: `buffer.append("Java");` — it appends the value at the end and modifies the same object.

### Q: Is StringBuffer thread-safe?
Yes. StringBuffer is synchronized, so it is thread-safe. Its methods are synchronized, which makes it slower than StringBuilder when only one thread is used.

### Q: What is StringBuilder and how does it relate to StringBuffer?
StringBuilder has the same API as StringBuffer (append, insert, reverse, delete, etc.) but its methods are not synchronized. It is faster than StringBuffer when thread safety is not required.

### Q: Where are String, StringBuffer, and StringBuilder objects stored?
String literals can be in the string pool; String objects created with new and all StringBuffer/StringBuilder objects are stored in the heap.

### Q: Compare String, StringBuffer, and StringBuilder on mutability, performance, and thread safety.
String is immutable; StringBuffer and StringBuilder are mutable. String and StringBuilder are fast; StringBuffer is slower due to synchronization. Only StringBuffer is thread-safe; StringBuilder is not synchronized.

### Q: When should you use StringBuffer versus StringBuilder?
Use StringBuffer when the object may be accessed by multiple threads. Use StringBuilder for single-threaded code when you need a mutable sequence and want better performance.

### Q: Does the String class have a reverse method?
No. Only StringBuffer and StringBuilder have a built-in reverse() method that reverses the character sequence in place.

### Q: How do you implement "reverse a string" using length(), charAt(), and a loop?
Use a loop from index length()-1 down to 0; in each iteration use charAt(i) to get the character and concatenate it to a new String (or append to StringBuilder). Example: for (int i = s.length()-1; i >= 0; i--) reversed += s.charAt(i);

### Q: What other useful StringBuffer/StringBuilder methods are there?
insert(offset, value) inserts at a position; reverse() reverses in place; delete(start, end) removes a range; length() returns the number of characters.

### Q: Where is the object stored when you do StringBuffer sb = new StringBuffer("Java");?
The object is stored in the heap. Only String literals use the string pool; StringBuffer and StringBuilder objects are always on the heap.

### Q: After buffer.append(" program"), what happens to the original StringBuffer content?
The same object is modified in place; its content becomes the previous value plus " program". No new object is created for the buffer reference.
