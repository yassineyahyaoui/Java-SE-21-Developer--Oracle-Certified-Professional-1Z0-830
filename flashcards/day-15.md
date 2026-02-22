# Day 15 -- OOP Programming (Part 2) — Sealed Types + Records

### Q: How do you access a superclass field or method from a subclass when the subclass has one with the same name?
Use `super.field` or `super.method()`. Without `super`, the subclass member is used. `super` is for parent access; `this` is for the current class.

### Q: How do you invoke the superclass constructor from a subclass constructor?
Use `super()` or `super(arg1, arg2, ...)` as the first statement in the subclass constructor. If the superclass has no no-arg constructor, the subclass must explicitly call a superclass constructor with the right arguments.

### Q: Can you combine `extends` and `implements` in one class declaration?
Yes. Syntax: `class Eagle extends Bird implements CanMove { }`. The class name comes first, then `extends` (at most one class), then `implements` (one or more interfaces, comma-separated).

### Q: What does the `final` keyword do when applied to a class?
A **final class** cannot be extended. Any attempt to `extends` a final class causes a compile error (e.g. “cannot inherit from final class Vehicle”).

### Q: What does the `final` keyword do when applied to a method?
A **final method** cannot be overridden in subclasses. Overriding it causes a compile error (e.g. “cannot override; overridden method is final”).

### Q: What does the `final` keyword do when applied to a variable?
A **final variable** must be initialized and cannot be reassigned. It acts as a constant. For reference types, the reference cannot change (the object’s state can still change unless the object is immutable). Convention: final constants often use UPPER_SNAKE_CASE.

### Q: Can an abstract class have constructors?
Yes. Abstract classes can have constructors. Subclasses invoke them via `super()`. You cannot instantiate an abstract class with `new`, but the constructor runs when a concrete subclass is instantiated.

### Q: What is an abstract method and what modifiers are not allowed on it?
An abstract method has no body (only a semicolon after the signature). It cannot be **final** (would prevent overriding), **private** (would prevent overriding), or **static**. It must be in an abstract class (or interface).

### Q: If a class has at least one abstract method, what must the class be?
The class must be declared **abstract**. You cannot have an abstract method in a non-abstract class.

### Q: Can you create an instance of an abstract class?
No. You cannot do `new AbstractClass()`. You must extend it with a concrete class and create instances of that subclass. Abstract classes are templates; concrete subclasses provide the implementation.

### Q: What are the default modifiers for interface methods and variables?
Methods in an interface are implicitly **public abstract** (no body unless default/static). Variables are implicitly **public static final**, so they are constants and must be initialized.

### Q: Can a class implement multiple interfaces?
Yes. Use `implements I1, I2, I3`. A class can extend at most one class but implement any number of interfaces. This is how Java supports a form of “multiple inheritance” of type/behavior.

### Q: Can interface methods have a body?
Abstract methods in an interface have no body. **default** and **static** methods in an interface must have a body. Default and static methods were added in Java 8; implementing classes do not have to override default methods.

### Q: Can an interface have constructors?
No. Interfaces do not contain constructors. You cannot instantiate an interface with `new`.

### Q: Can a class extend another class and implement interfaces at the same time?
Yes. Example: `class Bird extends Animal implements CanFly, CanEat { }`. Extend at most one class first, then list interfaces after `implements`.

### Q: If a subclass extends a class that implements interfaces, must the subclass re-implement those interface methods?
No. The subclass inherits the implementations from its parent. It only needs to implement methods from any **new** interfaces the subclass itself implements.

### Q: What happens if you declare a variable in an interface without initializing it?
You get a compile error. Interface variables are implicitly `public static final`, so they must be initialized when declared.
