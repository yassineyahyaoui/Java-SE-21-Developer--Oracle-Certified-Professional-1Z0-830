# Module 15 -- Lambda Expression

### Q: What is a?

Define a functional interface as an interface with exactly one abstract method (SAM); identify `Runnable` as a classic example; state that it can also have `default` and `static` methods

### Q: How do you apply the `@FunctionalInterface` annotation and explain that the compiler enforces the single-abstract-method rule when it is present?

Apply the `@FunctionalInterface` annotation and explain that the compiler enforces the single-abstract-method rule when it is present

### Q: What is what a marker interface is?

Explain what a marker interface is and how it differs from a functional interface

### Q: How do you lambda expressions using the syntax `(parameters) -> body` as a concise replacement for anonymous classes implementing functional interfaces (Java 8)?

Write lambda expressions using the syntax `(parameters) -> body` as a concise replacement for anonymous classes implementing functional interfaces (Java 8)

### Q: How do you use the `Predicate<T>` interface from `java.util.function`: call `test()` to evaluate a boolean condition, and combine it with lambda expressions for filtering logic?

Use the `Predicate<T>` interface from `java.util.function`: call `test()` to evaluate a boolean condition, and combine it with lambda expressions for filtering logic

### Q: How do you use method references (`::` operator) as a more readable alternative to lambda expressions; explain that they refer to an existing method definition directly (Java 8)?

Use method references (`::` operator) as a more readable alternative to lambda expressions; explain that they refer to an existing method definition directly (Java 8)

### Q: How do you switch expressions using arrow syntax (`->`) that return a value, eliminating `break` and fall-through (Java 12/14); use `yield` to return a value from a multi-statement case block?

Write switch expressions using arrow syntax (`->`) that return a value, eliminating `break` and fall-through (Java 12/14); use `yield` to return a value from a multi-statement case block

### Q: What is the improvements in switch expressions over traditional switch: no fall-through?

Explain the improvements in switch expressions over traditional switch: no fall-through, returns a value, semicolon required at closing brace, and Java 21 further enhancements

### Q: Build a Simple Calculator console application using lambda expressions and functional interfaces to perform addition, subtraction, multiplication, and division on user input?

Build a Simple Calculator console application using lambda expressions and functional interfaces to perform addition, subtraction, multiplication, and division on user input

### Q: What is for instance the runnable interface in the Java.lang...?

So for instance the runnable interface in the Java.lang package is a prime example of a functional interface.

### Q: What is The first one?

The first one is the argument list can be empty or it can be non-empty.

### Q: What is The second one?

The second one is the arrow token, and this is used to link the arguments list and the body of the expression.

### Q: What is the predicate interface?

So the predicate interface is a functional interface.

### Q: What is However, since it contains only one abstract method,...?

However, since it contains only one abstract method, which is a test method, it is annotated as a functional interface.

### Q: What is That'll be I, since the type of the predicate?

That'll be I, since the type of the predicate is an integer, well, the type of the I variable is going to be integer again.

### Q: What is if and you notice a parameter of the remove if method?

if and you notice a parameter of the remove if method is the predicate interface that worked so well.

### Q: What is S out entered number plus double quotes?

S out entered number plus double quotes is an even number.

### Q: What is And the five?

And the five is an odd number.

### Q: What is Yeah, the condition is met and the message six?

Yeah, the condition is met and the message six is an even number gets printed to the console.

### Q: What is The predicate?

The predicate is a functional interface, and it has an abstract method called test that returns a boolean.

### Q: What is method reference?

So method reference is a feature that came with Java eight.

### Q: What is Here the name parameter represents each element in t...?

Here the name parameter represents each element in the list, while the lambda symbol indicates which operations can be performed, which is the process of printing the elements of the list.

### Q: What is But there?

But there is a situation like this.

### Q: What is yeah this?

So yeah this is the basic use of the method reference.

### Q: What is The function?

The function is a functional interface that takes an input and returns a result.

### Q: What is Since the method that we'll use?

Since the method that we'll use is the print method I'll just delete all the expressions other than that.

### Q: What is The function interface?

The function interface is a functional interface and contains an apply method that controls the input and output.

### Q: What is in other words there's no input but there?

So in other words there's no input but there is a product.

### Q: What is And supplier?

And supplier is a functional interface that produces a result without receiving any input.

### Q: What is And since the constructor method?

And since the constructor method is the only thing that's going to be called the lambda parameter, parenthesis will be empty again.

### Q: What is You got to notice here too that the show method in t...?

You got to notice here too that the show method in the animals class and the display method have a similar signature that is the same return type and the same parameters.

### Q: What is The first?

The first is the usage of the break keyword.

### Q: What is The second one that I want to run by you?

The second one that I want to run by you is the usage of the message variable.

### Q: What is if our object?

So if our object is an instance of integer, let's pass the object to a string with a bit of an explanation text.
