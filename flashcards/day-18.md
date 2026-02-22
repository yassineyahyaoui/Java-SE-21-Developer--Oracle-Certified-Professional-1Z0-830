# Day 18 -- CHECKPOINT: OOP + Control Flow

### Q: What is the single-inheritance rule in Java?
A class can extend at most one direct superclass. Java does not support multiple inheritance of state. Interfaces allow multiple inheritance of type (implements several interfaces).

### Q: When is super() or this() required as the first statement in a constructor?
If you don't write one, the compiler inserts `super()` (no-arg). You must call `super(...)` or `this(...)` explicitly when the parent has no no-arg constructor, or when you want to pass arguments. Only one of super() or this() can appear, and it must be first.

### Q: What are sealed types and why are they used?
Sealed classes/interfaces restrict which subclasses or implementations can exist. You list them in the `permits` clause. They enable exhaustive pattern matching and keep the hierarchy under control.

### Q: What are the rules for a class that permits subclasses in a sealed hierarchy?
A permitted subclass must extend the sealed class (or implement the sealed interface), must be final, sealed, or non-sealed, and must be in the same module (or same package when no module).

### Q: What is a record and what does the compiler generate?
A record is a compact way to declare an immutable data carrier: `record Point(int x, int y) {}`. The compiler generates a canonical constructor, private final fields, accessors (e.g. x(), y()), equals, hashCode, and toString. Records are final and cannot extend other classes.

### Q: Can a record extend another class?
No. A record implicitly extends java.lang.Record and cannot extend any other class. It can implement interfaces.

### Q: How do switch expressions differ from switch statements?
Switch expressions produce a value: `var result = switch (x) { case 1 -> "one"; case 2 -> "two"; default -> "other"; };`. They use `->` (no fall-through) and must be exhaustive (all cases or default). No break needed.

### Q: What makes a switch exhaustive for enums or sealed types?
Either every constant (enum) or every permitted type (sealed) is covered by a case, or there is a default. The compiler checks exhaustiveness so you don't miss a case.

### Q: What are the main rules for method overriding?
Override with the same signature (name and parameter types). Return type must be covariant (subtype or same). Access cannot be more restrictive. Cannot override static (it's hidden), final, or private methods. @Override helps catch mistakes.

### Q: Can an interface have default and static methods?
Yes. Default methods have a body and can be overridden; they provide backward compatibility. Static methods in an interface are called on the interface name and are not inherited by implementing classes.

### Q: What are the rules for abstract classes?
They can have abstract methods (no body) and concrete methods. They cannot be instantiated. A concrete subclass must implement all abstract methods or be declared abstract. They can have constructors, fields, and any access modifiers for members.

### Q: If a class has one abstract method and is not declared abstract, what happens?
Compile error. A class with any abstract method must be declared abstract.

### Q: In control flow, when are braces optional in an if or else?
Only when the block has exactly one statement. Without braces, a second statement is not part of the if/else and always runs—a common exam trap.

### Q: What types are allowed as the switch expression?
byte, short, int, char (and wrappers), String, enum, and (in modern Java) other reference types. The expression and case values must be compatible.

### Q: What is pattern matching for instanceof and how is it used?
`if (obj instanceof String s)` — if the check is true, `s` is in scope and refers to the casted value. Avoids a separate cast and is useful in conditionals and switch.

### Q: How does polymorphism relate to overriding and reference types?
The runtime type (actual object) decides which overridden method runs. The reference type decides what members you can call. So a Parent ref holding a Child object will run Child's overridden method when you call it.

### Q: In a try-catch, what happens if the catch doesn't match the thrown exception?
The exception propagates up the call stack. If no handler is found, the thread terminates (uncaught exception). Catches are matched by exception type (including subclasses).
