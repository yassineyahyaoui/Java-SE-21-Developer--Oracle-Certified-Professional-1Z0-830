# Day 24 -- Exception Handling

### Q: What is the top of the exception hierarchy and what are its two main subclasses?
Throwable is the top class (in java.lang). Its two subclasses are Error (unrecoverable) and Exception (recoverable).

### Q: What is the difference between an Error and an Exception?
Error represents critical, unrecoverable conditions (e.g. lack of system resources); the program usually cannot handle it. Exception represents conditions that can be handled by the code (e.g. bad input, I/O).

### Q: What are checked vs unchecked exceptions?
Checked exceptions are checked at compile time; you must handle or declare them. Unchecked exceptions (RuntimeException and its subclasses) are not checked at compile time and are thrown at runtime.

### Q: How do you handle exceptions with try and catch?
Enclose code that may throw in a try block; one or more catch blocks follow to handle specific exception types. The first matching catch block is executed.

### Q: What is multi-catch and what is the rule for the exception parameter?
From Java 7+, you can catch multiple exception types in one catch: `catch (IOException | SQLException e)`. The parameter `e` is effectively final and cannot be reassigned.

### Q: When does the finally block run?
finally runs after try (and catch if an exception occurred), whether or not an exception was thrown. Exception: it does not run if the JVM exits (e.g. System.exit()) or the thread is killed.

### Q: What is the difference between throw and throws?
throw is used inside a method to throw an exception instance. throws is used in the method signature to declare that the method may throw one or more exception types (classes).

### Q: How many exceptions can you declare with throw vs throws?
throw throws one exception instance at a time. throws can declare multiple exception classes separated by commas.

### Q: What do getMessage(), toString(), and printStackTrace() do on a Throwable?
getMessage() returns the detail message string (may be null). toString() returns a short description (class name + message). printStackTrace() prints the stack trace to the standard error stream (void).

### Q: How do you create a custom (user-defined) exception?
Extend Exception (for checked) or RuntimeException (for unchecked). Typically provide a constructor that accepts a message and call super(message).

### Q: What is try-with-resources and what interface must resources implement?
try-with-resources automatically closes resources when the try block ends (normal or exception). Resources must implement AutoCloseable (and its close() method).

### Q: In what order are resources closed in try-with-resources?
Resources are closed in reverse order of declaration. The last declared resource is closed first.

### Q: Give examples of checked and unchecked exceptions.
Checked: FileNotFoundException, IOException, ClassNotFoundException. Unchecked: NullPointerException, ArithmeticException, IllegalArgumentException, ArrayIndexOutOfBoundsException.

### Q: Why use multiple catch blocks after a try?
Each catch can handle a different exception type. More specific types should come before more general (e.g. catch IOException before Exception), or the compiler will report unreachable code.
