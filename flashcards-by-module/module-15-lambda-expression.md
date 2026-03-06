# Module 15 -- Lambda Expression

### Q: What is a functional interface in Java?
A functional interface has exactly one abstract method (SAM). It can have default and static methods. Examples: Runnable (run()), Predicate (test(T)), Comparator (compare(T,T)).

### Q: What does @FunctionalInterface do?
It declares that the interface has exactly one abstract method. The compiler will report an error if you add a second abstract method.

### Q: What is the general syntax of a lambda expression?
(parameters) -> body. Examples: `() -> 42`, `(x, y) -> x + y`, `s -> s.length()`. The body can be an expression (value returned) or a block with statements.

### Q: What is Predicate<T> and what does test() do?
Predicate<T> is in java.util.function; it has one method boolean test(T t). Used for conditional checks, e.g. `Predicate<Integer> p = x -> x > 0; p.test(5)` is true.

### Q: How do you chain two Predicates?
Use and(), or(), or negate(): `p1.and(p2).test(x)`, `p1.or(p2).test(x)`, `p1.negate().test(x)`.

### Q: What is a method reference and when do you use it?
A shorthand for a lambda that only calls one method. Syntax: ClassName::methodName or object::methodName. Example: `System.out::println` instead of `x -> System.out.println(x)`.

### Q: Can a variable used inside a lambda be reassigned after the lambda is created?
No. Variables used inside a lambda must be effectively final: either declared final or never reassigned after capture. Reassigning causes a compile error.

### Q: Where can you use var in a lambda parameter list?
You can use var for parameters: `(var x, var y) -> x + y`. All parameters must use var or none; you cannot mix var and explicit types in the same lambda.
