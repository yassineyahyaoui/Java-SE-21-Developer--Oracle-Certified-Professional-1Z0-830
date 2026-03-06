# Module 13 -- Exception Handling in Java

### Q: What is the top of the exception hierarchy and what are its two main subclasses?
Throwable is the top class (java.lang). Its two subclasses are Error (unrecoverable) and Exception (recoverable).

### Q: What is the difference between an Error and an Exception?
Error represents critical, unrecoverable conditions (e.g. OutOfMemoryError); the program usually cannot handle it. Exception represents conditions that can be handled (e.g. IOException, IllegalArgumentException).

### Q: What are checked vs unchecked exceptions?
Checked exceptions are checked at compile time; you must handle them (try-catch) or declare them (throws). Unchecked exceptions (RuntimeException and its subclasses) are not required to be declared or caught.

### Q: What is the order of catch blocks when handling multiple exception types?
More specific types must come before more general. If you catch Exception before IOException, the IOException catch is unreachable and the compiler reports an error.

### Q: When does the finally block run?
finally runs after try (and catch if an exception occurred), whether or not an exception was thrown. It does not run if the JVM exits (e.g. System.exit()) or the thread is killed.

### Q: What is the difference between throw and throws?
throw is a statement that throws an exception instance inside a method. throws is used in the method signature to declare that the method may throw one or more exception types.

### Q: What is try-with-resources and what must resources implement?
try-with-resources automatically closes resources when the try block ends. Resources must implement AutoCloseable (and its close() method). Example: `try (InputStream is = ...) { }`.

### Q: In what order are resources closed in try-with-resources?
Resources are closed in reverse order of declaration. The last declared resource is closed first.

### Q: Give examples of checked and unchecked exceptions.
Checked: FileNotFoundException, IOException, SQLException. Unchecked: NullPointerException, ArithmeticException, IllegalArgumentException, ArrayIndexOutOfBoundsException.
