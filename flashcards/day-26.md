# Day 26 -- Lambda Expressions (Part 1)

### Q: What is a functional interface in Java?
A functional interface has exactly one abstract method (SAM). It can also have multiple default and static methods. Example: `Runnable` in `java.lang` has only the abstract method `run()`.

### Q: What does the @FunctionalInterface annotation do?
It is a declaration that the interface follows the functional interface contract: exactly one abstract method. The compiler will report an error if you add a second abstract method.

### Q: How does a marker interface differ from a functional interface?
A marker interface has no methods or fields (e.g. `Serializable`, `Cloneable`, `Remote`). A functional interface has exactly one abstract method; it may also have default and static methods.

### Q: What are functional interfaces also called?
Single Abstract Method (SAM) interfaces, because their defining characteristic is having exactly one abstract method.

### Q: Is the abstract keyword required on the single method of a functional interface?
No. In an interface, methods are abstract by default, so the keyword is optional.

### Q: What is the general syntax of a lambda expression?
`(parameters) -> body`. The argument list can be empty or non-empty; the arrow token links arguments to the body; the body contains expressions or statements.

### Q: What are the three components of a lambda expression?
(1) Argument list (empty or non-empty), (2) arrow token `->`, (3) body (expressions or statements).

### Q: In a lambda, do parameter names have to match the interface method parameter names?
No. You can use any names (e.g. `a` and `s`); the first parameter corresponds to the first parameter of the abstract method, the second to the second, and so on.

### Q: Where is the Predicate interface defined and what does it represent?
It is in `java.util.function`. It is a functional interface with one abstract method `test(T t)` that returns a boolean, used for conditional checks.

### Q: What does Predicate\<T\>.test() do?
It takes one argument of type T and returns true if the condition is satisfied, false otherwise. Used with lambdas like `x -> x < 10` or `s -> s.equals("Java")`.

### Q: How do you chain two Predicates (e.g. "less than 10" and "greater than 5")?
Use `predicate1.and(predicate2)` or `predicate1.or(predicate2)`. Example: `p1.and(p2).test(7)` where p1 is `i -> i < 10` and p2 is `m -> m > 5`.

### Q: How can you use Predicate with a List (e.g. remove matching elements)?
`list.removeIf(predicate)`. For example `animals.removeIf(animal -> animal.equals("ant"))` removes the element `"ant"` from the list.

### Q: What is the benefit of using a lambda instead of an anonymous class for a functional interface?
Lambdas are more concise and readable when you only need to implement one method; they treat functionality as method arguments (code as data) and reduce boilerplate.

### Q: When were functional interfaces and lambda expressions introduced in Java?
Java 8, alongside method references. They improve readability, cleanliness, and simplicity of code.

### Q: Can you assign a lambda to a variable whose type is a functional interface?
Yes. For example `Animals animal = (a, s) -> System.out.println(a + " can reach speeds of " + s + " km/h");` then call `animal.show("Cheetah", 90);`
