# Module 13 -- Exception Handling in Java

### Q: What is the `Throwable` hierarchy: `Error` (system-level?

Explain the `Throwable` hierarchy: `Error` (system-level, unrecoverable: `StackOverflowError`, `OutOfMemoryError`) vs `Exception` (recoverable); classify exceptions as checked (compile-time, e.g., `FileNotFoundException`), unchecked (runtime, e.g., `ArithmeticException`), or user-defined

### Q: How do you `try/catch` blocks with multiple catch blocks; use multi-catch with `|` (Java 7+) and explain that the exception parameter is effectively final?

Write `try/catch` blocks with multiple catch blocks; use multi-catch with `|` (Java 7+) and explain that the exception parameter is effectively final

### Q: What is the `finally` block: always runs for cleanup (e.g.?

Explain the `finally` block: always runs for cleanup (e.g., closing connections) whether or not an exception occurs

### Q: How do you use `throw` to explicitly throw an exception and `throws` in a method signature to declare exceptions; call `getMessage()`, `toString()`, and `printStackTrace()` on a caught exception to inspect error details?

Use `throw` to explicitly throw an exception and `throws` in a method signature to declare exceptions; call `getMessage()`, `toString()`, and `printStackTrace()` on a caught exception to inspect error details

### Q: Create a user-defined exception by extending `Exception` and use it in a practical Bank Account project?

Create a user-defined exception by extending `Exception` and use it in a practical Bank Account project

### Q: How do you use try-with-resources (`AutoCloseable`) to automatically close resources and explain that resources are closed in reverse declaration order?

Use try-with-resources (`AutoCloseable`) to automatically close resources and explain that resources are closed in reverse declaration order

### Q: What is First we're going to learn what?

First we're going to learn what is an exception and then how to create exceptions in Java.

### Q: What is An exception?

An exception is a special type of error.

### Q: What is an error?

So an error is a critical condition that cannot be handled by the code of the program.

### Q: What is And as you can see here in the diagram object?

And as you can see here in the diagram object is the topmost class in Java.

### Q: What is here throwable?

So here throwable is the topmost class of the exception classes and it's located in the Java.lang package.

### Q: What is The first one?

The first one is the checked exception.

### Q: What is Arithmetic exception?

Arithmetic exception is an unchecked exception, and it occurs when you make an arithmetic error, such as dividing a number by zero.

### Q: What is Like we mentioned earlier, the last one?

Like we mentioned earlier, the last one is the user defined exception.

### Q: What is The exception that might be thrown here?

The exception that might be thrown here is a input mismatch exception.

### Q: What is what you see here?

So what you see here is a divide method that returns a double value.

### Q: What is in the method, because we can't divide a number by z...?

Now in the method, because we can't divide a number by zero, we'll add throw arithmetic exception and pass a single string constructor parameter which is the exception message divider cannot be equal to zero.

### Q: What is The first one is number format exception and the sec...?

The first one is number format exception and the second one is the arithmetic exception.

### Q: What is The first parse Int?

The first parse Int is the method that throws the number format exception.

### Q: What is The second one?

The second one is the two string method, and this method returns a short description of a throwable.

### Q: What is And the third one?

And the third one is the print stack trace method.

### Q: What is the second method?

Now the second method is the toString method.

### Q: What is And now the last method?

And now the last method is the print stack trace.

### Q: What is Nobody likes to see that I know insufficient fund ex...?

Nobody likes to see that I know insufficient fund exception is a type of user defined exception.

### Q: What is The conditional switch expression?

The conditional switch expression is the variable choice.
