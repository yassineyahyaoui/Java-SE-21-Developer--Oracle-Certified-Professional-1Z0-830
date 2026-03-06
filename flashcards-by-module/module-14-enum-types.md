# Module 14 -- Enum Types

### Q: What is an enum type in Java?
An enum is a special type that defines a fixed set of named constants. Each constant is an instance of the enum type, created when the enum is loaded.

### Q: How do you declare and use an enum in a switch statement?
Use the enum as the switch expression: `switch (color) { case RED: ... break; case GREEN: ... }`. Case values are the enum constants. Break or return is needed to avoid fall-through.

### Q: How do you compare enum constants for equality?
Use `==`—enum constants are singletons, so reference equality is correct. You can also use `equals()`, but `==` is preferred on the exam.

### Q: How do you convert a String to an enum and what exception can be thrown?
Use `EnumType.valueOf(String name)`. The string must match an enum constant name exactly (case-sensitive). Invalid input throws `IllegalArgumentException`.

### Q: Can an enum extend another class?
No. All enums implicitly extend `java.lang.Enum`. A class can extend only one parent, so an enum cannot extend any other class. Enums can implement interfaces.

### Q: How do you give an enum custom values (e.g. a String per constant)?
Define a private (or package-private) constructor and a field; list each constant with arguments in parentheses: `RED("stop"), GREEN("go");`. Add a getter to expose the value.

### Q: Why must an enum constructor be private or package-private?
Enum constants are the only valid instances; no external code should create more. A public enum constructor is not allowed.

### Q: How do you get all enum constants as an array?
Use the static method `EnumType.values()`, which returns an array of all constants. Example: `for (TrafficLight light : TrafficLight.values()) { }`.

### Q: What is the difference between name() and toString() on an enum?
`name()` is final and returns the exact constant name (e.g. "RED"). `toString()` can be overridden to return a different display string; by default it returns the same as name().
