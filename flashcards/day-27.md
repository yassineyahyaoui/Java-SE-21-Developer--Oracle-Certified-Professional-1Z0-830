# Day 27 -- Lambda Expressions (Part 2)

### Q: What is a method reference and how is it written?
A shorthand for a lambda that only calls an existing method. Syntax: `objectOrClass::methodName`. Example: `System.out::println` instead of `x -> System.out.println(x)`.

### Q: When can you replace a lambda with a method reference?
When the lambda body only calls one method with the same parameter(s) and return type as the functional interface. If there is extra logic (e.g. condition, multiple steps), use a lambda.

### Q: How do you reference a static method with the :: operator?
Use `ClassName::staticMethod`. Example: `Integer::parseInt` is equivalent to the lambda `s -> Integer.parseInt(s)` and fits `Function<String, Integer>`.

### Q: How do you reference an instance method on a specific object?
Use `objectRef::instanceMethod`. Example: `str::toUpperCase` where `str` is a String; no input, so it fits `Supplier<String>` and you get the result via `get()`.

### Q: How do you reference a constructor with the :: operator?
Use `ClassName::new`. Example: `ArrayList::new` is equivalent to `() -> new ArrayList<>()` and can be passed to a `Supplier`.

### Q: What must match when using a method reference with a functional interface?
The referenced method's signature (parameter types and return type) must match the single abstract method of the functional interface. The interface must be a functional interface (one abstract method).

### Q: What is the arrow syntax in a switch expression and how does it differ from colon?
Use `case value -> expression;` instead of `case value:`. With the arrow, only that case runs (no fall-through), so you do not need `break`.

### Q: Why does the enhanced switch (switch expression) avoid fall-through?
Each case uses `->` and produces a single value or block; only the matched case is executed and the switch ends. There is no fall-through to the next case.

### Q: How do you return a value from a switch expression?
Assign the switch to a variable: `String msg = switch (day) { case 1,2,3,4,5 -> "Work day"; case 6,7 -> "Weekend"; default -> "Invalid"; };` or use `yield` in a block.

### Q: When do you need the yield keyword in a switch expression?
When a case has a block with multiple statements; use `yield value;` to return the value for that case. Example: `case 3 -> { System.out.println("Wed"); yield "Wednesday"; }`

### Q: Can you mix colon and arrow syntax in the same switch?
No. Using both in one switch causes a compilation error. Stick to either traditional colon (with break) or arrow (and optionally yield) style.

### Q: What is pattern matching in switch (Java 21) and how does it relate to instanceof?
Switch can match on type and bind a variable: `switch (obj) { case Integer i -> "int: " + i; case String s -> "str: " + s; default -> "unknown"; }` instead of multiple if-instanceof checks.

### Q: With enums in a switch expression, what happens if you do not handle all constants?
The compiler reports an error (switch expression does not cover all possible input values). You must handle every enum constant or add a default case.

### Q: How was the Simple Calculator built using lambdas and functional interfaces?
An `Operation` functional interface with `void performOperation(double x, double y)` was used; a `Calculator` class had `calculate(x, y, operation)`; in main, lambdas were passed for add, subtract, multiply, and divide (e.g. `(num1, num2) -> { ... }`).

### Q: What is the benefit of switch expressions over traditional switch for assigning a variable?
The switch returns a value, so you assign once (e.g. `message = switch(day) { ... };`) instead of assigning in every case and using break, reducing repetition and errors.

### Q: For a switch expression that returns a value, what is required at the end of the switch block?
A semicolon after the closing `}` of the switch, because the whole switch is an expression used in a statement.
