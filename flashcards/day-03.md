# Day 3 -- Java Basics (Part 1)

### Q: What is the key difference between System.out.print and System.out.println?
`println` prints the string and then moves the cursor to the beginning of the next line; `print` leaves the cursor on the same line after printing.

### Q: Does System.out.printf move the cursor to the next line after printing?
No. Like `print`, `printf` keeps the cursor on the same line. To move to the next line after `printf`, use an empty `println()` or add `%n` in the format string.

### Q: What format specifier is used in printf for a decimal integer, and for a string?
Use `%d` for a decimal integer and `%s` for a string. Example: `System.out.printf("%d %s%n", 10, "hello");`

### Q: How is printf related to the String class?
The `printf` method behaves the same as invoking the `format` method of the String class; both use the same format string and argument rules.

### Q: To read user input in Java using Scanner, what must you do first?
Import the Scanner class with `import java.util.Scanner;` and create a Scanner object, typically passing `System.in` (e.g., `Scanner input = new Scanner(System.in);`).

### Q: What is the difference between Scanner's next() and nextLine()?
`next()` reads only the next token (stops at whitespace), so "Hello World" yields only "Hello". `nextLine()` reads the entire line including spaces, so "Hello World" is read as one string.

### Q: Which Scanner method do you use to read an integer from the user?
Use `nextInt()` for integer input. Other type-specific methods include `nextDouble()`, `nextFloat()`, and `nextLong()`.

### Q: Why should you call close() on a Scanner object?
Closing the Scanner releases system resources and is good practice for efficiency; you'll understand resource management better in the Java I/O section.

### Q: How do you write a single-line comment in Java?
Start the line with `//`. The compiler ignores everything from `//` to the end of that line.

### Q: How do you write a multi-line comment in Java, and what symbols delimit it?
Use `/*` to start and `*/` to end. The compiler ignores everything between these two delimiters, so you can comment out multiple lines or blocks of code.

### Q: How do you recognize a documentation (Javadoc) comment?
It starts with `/**` (slash and two asterisks) and ends with `*/`. It is used to document classes and methods; tools can generate HTML docs from it.

### Q: What Javadoc tags are used to document method parameters and return value?
Use `@param parameterName description` for each parameter and `@return description` for the return value. Example: `@param x the first value` and `@return the product of x and y`.

### Q: In what order does the section roadmap cover Java basics?
The roadmap order is: (1) output, (2) input, (3) comments, (4) variables, (5) data types, (6) numbers (e.g., binary, octal, hex), (7) type conversion.

### Q: Which class provides print, println, and printf, and in which package is it?
The methods belong to the `PrintStream` class, which is in the `java.io` package. `System.out` is a `PrintStream` that sends output to the console.

### Q: How do you print a formatted string without using printf?
Use `String.format(formatString, args...)` to build the formatted string, then pass it to `print` or `println`. Example: `System.out.println(String.format("Value: %d", 42));`
