# Day 17 -- Enums + OOP Review

### Q: What is an enum type in Java and how should its constants be named?
An enum is a special type that defines a variable as one of a predefined set of constants. Enum constants are conventionally in UPPERCASE (e.g. RED, YELLOW, GREEN) because they are constants.

### Q: How do you declare and use an enum in a switch statement?
Use the enum as the switch expression: `switch (color) { case RED: ... break; case GREEN: ... break; }`. Case values are the enum constants (no qualification needed in the same type). Break (or return) is needed to avoid fall-through.

### Q: How do you compare enum constants for equality?
Use `==` — enum constants are singletons, so reference equality is correct. You can also use `equals()`, but `==` is preferred and is the typical exam style.

### Q: How do you convert a String to an enum, and what exception can be thrown?
Use `EnumType.valueOf(String name)`. The string must match an enum constant name (case-sensitive). Invalid input throws `IllegalArgumentException` (e.g. "No enum constant EnumType.JAVA").

### Q: How should you handle invalid input when using valueOf(String)?
Catch `IllegalArgumentException` in a try-catch and handle it (e.g. prompt the user to enter a valid enum constant). Converting input with `toUpperCase()` before valueOf helps if constants are uppercase.

### Q: Can you create an enum instance with the new operator?
No. You cannot invoke an enum constructor with `new`. Instances are created only by the enum constants themselves. The JVM manages enum instances.

### Q: What inheritance restriction do enums have?
All enums implicitly extend `java.lang.Enum`. Because a class can extend only one parent, an enum cannot extend any other class.

### Q: How do you give an enum custom values (e.g. a String per constant)?
Define a private (or package-private) constructor and a field; list the constant name followed by the argument in parentheses: `RED("stop"), YELLOW("wait"), GREEN("go");`. Add a getter to expose the value.

### Q: Why must an enum constructor be private or package-private?
Enum constants are the only valid instances; no code outside the enum should create more. A public enum constructor is not allowed and causes a compilation error.

### Q: How do you get all enum constants as an array to iterate?
Use the static method `EnumType.values()`, which returns an array of all constants. Example: `for (TrafficLight light : TrafficLight.values()) { ... }`.

### Q: What is the difference between name() and toString() on an enum?
`name()` is final and always returns the exact constant name (e.g. "RED"). `toString()` can be overridden to return a different display string; by default it returns the same as name().

### Q: Are enum constants static and final?
Yes. Each enum constant is implicitly public static final. They are created once when the enum type is loaded.

### Q: How do enums fit with other OOP concepts for the exam?
Enums are a kind of type (like classes) with a fixed set of instances. They work with switch, polymorphism (they extend Enum), and encapsulation (private constructor, getters). Combine with inheritance, sealed types, records, and interfaces when reasoning about type hierarchies and exhaustiveness.

### Q: If your enum constants take constructor arguments, where do you pass them?
Right after the constant name, in parentheses: `RED("stop"), GREEN("go");`. The number and type must match the enum’s constructor.

### Q: What does valueOf expect when your constants are uppercase?
The string must match the constant name exactly. Use `input.toUpperCase()` before calling valueOf if the user types lowercase, so "red" becomes "RED" and matches.
