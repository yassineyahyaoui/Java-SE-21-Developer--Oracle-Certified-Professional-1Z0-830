# Day 4 -- Java Basics (Part 2)

### Q: What characters can a variable name begin with in Java?
A variable name can begin with a letter, a dollar sign (`$`), or an underscore (`_`). By convention, start with a letter; the dollar sign is rarely used, and leading underscore is discouraged.

### Q: Is Java case-sensitive for variable names?
Yes. Java is case-sensitive, so `age`, `Age`, and `AGE` are three different identifiers.

### Q: What naming convention is used for multi-word variable names in Java?
Use camelCase: the first word in lowercase, and the first letter of each subsequent word capitalized (e.g., `studentAge`, `totalCount`).

### Q: Where are instance variables defined, and how do they differ from static variables?
Instance variables are defined in a class but outside any method, and without the `static` keyword. Static variables are also in a class outside methods but are declared with `static` and are initialized once when the program starts.

### Q: Where are local variables declared?
Local variables are declared inside the body of a method (or block). They are not visible outside that method or block.

### Q: Name all eight primitive data types in Java and their typical use.
`boolean` (true/false), `char` (single Unicode character), `byte`, `short`, `int`, `long` (whole numbers), `float`, `double` (fractional numbers). Byte, short, int, long store integers; float and double store floating-point values.

### Q: What are the size and value range of the byte primitive type?
`byte` is 8-bit signed two's complement: minimum -128, maximum 127 (inclusive). Default value is 0.

### Q: What are the size and value range of the short and int primitive types?
`short` is 16-bit: -32,768 to 32,767. `int` is 32-bit: -2^31 to 2^31 - 1.

### Q: What are the size and value range of long, float, and double?
`long` is 64-bit: -2^63 to 2^63 - 1. `float` is 32-bit single-precision floating point. `double` is 64-bit double-precision floating point and is the usual default for decimal values.

### Q: Why are String objects said to be immutable?
Once a String is created, its value cannot be changed. Any operation that seems to "change" a String actually creates a new String object; the original is unchanged.

### Q: What suffix do you use for long literals and for float literals?
Use `L` or `l` for long (e.g., `98765432198L`); uppercase `L` is preferred to avoid confusion with `1`. Use `F` or `f` for float (e.g., `45.5F`).

### Q: Where can you place underscores in numeric literals, and where are they invalid?
You may place underscores between digits for readability (e.g., `98_765_432_198L`). You cannot place them at the beginning, at the end, or immediately before/after a decimal point.

### Q: How do you write binary, octal, and hexadecimal literals in Java?
Binary: prefix `0b` or `0B` (e.g., `0b1101`). Octal: leading `0` (e.g., `015`). Hexadecimal: prefix `0x` or `0X` (e.g., `0x1B0`). All are stored as integer type.

### Q: How do you convert a decimal int to its binary, octal, or hex string representation?
Use `Integer.toBinaryString(int)`, `Integer.toOctalString(int)`, and `Integer.toHexString(int)`. Each returns a String representation in that base.

### Q: What is automatic type conversion (widening), and when does it occur?
Automatic type conversion happens when you assign a value of a smaller data type to a variable of a larger, compatible type (e.g., `int` to `long` or `long` to `double`). No cast is required and there is no data loss.

### Q: What is explicit type casting (narrowing), and when is it required?
Explicit casting is required when assigning a larger type to a smaller type (e.g., `double` to `int`). You must write the cast: `int x = (int) someDouble;`. Data loss may occur (e.g., fractional part discarded).

### Q: What is the order of primitive types from smallest to largest (for conversion)?
From smallest to largest: byte, short, int, long, float, double. Converting from smaller to larger is safe (widening); converting from larger to smaller may cause data loss (narrowing).

### Q: Why might you lose data when casting from double to int?
The fractional part is discarded; only the integer part is kept. For example, `(int) 135.35` becomes `135`. Casting from a large integer type to a smaller one can also overflow and produce unexpected values.

### Q: Can you use a Java keyword as a variable name?
No. Keywords (e.g., `break`, `do`, `public`, `int`) are reserved and cannot be used as variable, method, or class names.

### Q: What makes a variable declaration invalid: "int 3age" or "int a ge"?
Both are invalid: variable names cannot start with a digit (`3age`), and whitespace is not allowed in identifiers (`a ge`).
