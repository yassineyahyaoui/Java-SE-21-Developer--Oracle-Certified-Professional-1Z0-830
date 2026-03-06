# Module 03 -- Basics of Java

### Q: What characters can a variable name begin with in Java?
A variable name can begin with a letter, a dollar sign (`$`), or an underscore (`_`). By convention, start with a letter.

### Q: Is Java case-sensitive for variable names?
Yes. Java is case-sensitive, so `age`, `Age`, and `AGE` are three different identifiers.

### Q: What naming convention is used for multi-word variable names in Java?
Use camelCase: the first word in lowercase, and the first letter of each subsequent word capitalized (e.g., `studentAge`, `totalCount`).

### Q: Where are instance variables, static variables, and local variables declared?
Instance variables: in a class but outside any method, without `static`. Static variables: in a class outside methods, with `static`. Local variables: inside a method or block.

### Q: Name all eight primitive data types in Java.
`boolean`, `char`, `byte`, `short`, `int`, `long`, `float`, `double`. Byte, short, int, long store integers; float and double store floating-point; char stores Unicode; boolean stores true/false.

### Q: What are the size and value range of byte, short, and int?
`byte`: 8-bit, -128 to 127. `short`: 16-bit, -32,768 to 32,767. `int`: 32-bit, -2^31 to 2^31 - 1.

### Q: Why are String objects said to be immutable?
Once a String is created, its value cannot be changed. Any operation that seems to "change" a String actually creates a new String object; the original is unchanged.

### Q: What suffix do you use for long literals and for float literals?
Use `L` or `l` for long (e.g., `98765432198L`); uppercase `L` is preferred. Use `F` or `f` for float (e.g., `45.5F`).

### Q: Where can you place underscores in numeric literals, and where are they invalid?
You may place underscores between digits for readability (e.g., `98_765_432_198L`). You cannot place them at the beginning, at the end, or immediately before/after a decimal point.

### Q: How do you write binary, octal, and hexadecimal literals in Java?
Binary: prefix `0b` or `0B` (e.g., `0b1101`). Octal: leading `0` (e.g., `015`). Hexadecimal: prefix `0x` or `0X` (e.g., `0x1B0`).

### Q: How do you convert a decimal int to its binary, octal, or hex string representation?
Use `Integer.toBinaryString(int)`, `Integer.toOctalString(int)`, and `Integer.toHexString(int)`.

### Q: What is widening (automatic type conversion) and when does it occur?
Widening happens when you assign a value of a smaller type to a variable of a larger, compatible type (e.g., `int` to `long` or `long` to `double`). No cast is required; no data loss.

### Q: What is narrowing (explicit casting) and when is it required?
Narrowing is assigning a larger type to a smaller type (e.g., `double` to `int`). You must write the cast: `int x = (int) someDouble;`. Data loss may occur (e.g., fractional part discarded).

### Q: What is the order of primitive types from smallest to largest for conversion?
From smallest to largest: byte, short, int, long, float, double. Converting smaller to larger is safe (widening); larger to smaller may cause data loss (narrowing).
