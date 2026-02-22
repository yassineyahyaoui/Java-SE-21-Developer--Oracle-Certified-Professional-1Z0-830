# Day 19 -- Strings (Part 1)

### Q: What is a String in Java?
A String is an object that represents a sequence of characters. It is a reference type in java.lang and is one of the most used types for text.

### Q: How do you create a String with a literal versus with new String()?
With a literal: `String s = "hello";` — the value may be stored in the string pool. With `new`: `String s = new String("hello");` — a new object is created on the heap (and the literal may still be in the pool).

### Q: Where are String literals stored versus String objects created with new?
String literals are stored in the string pool (a special area in the heap). Objects created with `new String(...)` are stored in the heap; the pool is used only for the literal argument if present.

### Q: For two String references, when does == return true versus when does equals() return true?
== returns true only if both references point to the same object. equals() returns true when the character sequences are the same, regardless of whether they are the same object.

### Q: Why are Strings said to be immutable?
Once a String object is created, its character sequence cannot be changed. Any method that seems to modify it (e.g. concat(), toUpperCase()) returns a new String; the original is unchanged.

### Q: Does calling concat() on a String modify the original String?
No. concat() returns a new String with the concatenated value. The original String is not modified.

### Q: What does String length() return?
The number of characters in the sequence (int). For "" it returns 0.

### Q: What does charAt(int index) do?
Returns the char at the given index (0-based). Throws IndexOutOfBoundsException if index is negative or >= length().

### Q: What do indexOf overloads do?
indexOf(String str) returns the index of the first occurrence of the substring, or -1 if not found. Other overloads: indexOf(int ch), indexOf(String str, int fromIndex), etc.

### Q: How does substring(int beginIndex) work? What about substring(int begin, int end)?
substring(beginIndex) returns from beginIndex to the end. substring(begin, end) returns from beginIndex (inclusive) to endIndex (exclusive). In Java 7+, these create a new char array (no shared backing array).

### Q: What do toUpperCase() and toLowerCase() return?
They return a new String with all characters converted to upper or lower case according to the default locale. The original String is unchanged.

### Q: What does trim() do?
Returns a new String with leading and trailing whitespace removed. The original is unchanged.

### Q: What does contains(CharSequence s) do?
Returns true if the String contains the specified character sequence, false otherwise.
