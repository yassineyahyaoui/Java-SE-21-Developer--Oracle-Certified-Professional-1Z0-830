# Module 09 -- Java Object-Oriented Programming

### Q: How do you create a subclass in Java?
Use the `extends` keyword: `class MountainBike extends Bicycle`. Each class has exactly one direct superclass (single inheritance).

### Q: Are constructors inherited by subclasses?
No. Constructors are not inherited. The subclass can invoke the superclass constructor with `super()` or `super(args)` as the first statement in the constructor.

### Q: How do you declare a sealed class and what does permits do?
Use `sealed` on the class and a `permits` clause: `public sealed class Animal permits Dog, Cat, Bird { }`. Only the permitted classes may extend the sealed class. Each permitted subclass must be final, sealed, or non-sealed.

### Q: What is method overriding and what must match?
Overriding is defining in a subclass a method with the same name, same parameters, and compatible return type as in the superclass. You cannot reduce visibility (e.g. public to private).

### Q: What is the super keyword used for?
Access superclass fields (`super.field`), call superclass methods (`super.method()`), and invoke superclass constructor (`super()` or `super(args)`). The super constructor call must be the first statement in a constructor if present.

### Q: What does the final keyword do when applied to a class, method, or variable?
Final class: cannot be extended. Final method: cannot be overridden. Final variable: must be initialized and cannot be reassigned (constant).

### Q: Can an abstract class have constructors? Can you create an instance of an abstract class?
Yes, abstract classes can have constructors (invoked when a concrete subclass is instantiated). No, you cannot do `new AbstractClass()`; you must extend with a concrete class.

### Q: What are the default modifiers for interface methods and variables?
Methods: implicitly public abstract (unless default or static). Variables: implicitly public static final (constants).

### Q: Can a class implement multiple interfaces?
Yes. Use `implements I1, I2, I3`. A class can extend at most one class but implement any number of interfaces.

### Q: What is a record and what does the compiler generate?
A record is a compact immutable data carrier: `record Person(String name, int age)`. The compiler generates: canonical constructor, accessors (name(), age()), equals, hashCode, and toString based on the components.

### Q: Can a record extend another class or be extended?
A record cannot extend any class (its direct superclass is Record). A record is implicitly final and cannot be extended. A record can implement interfaces.

### Q: What is the var keyword and where can it be used?
var enables local variable type inference; the compiler infers the type from the initializer. It can be used only for local variables (inside methods/blocks) and must be initialized when declared. Not for fields, parameters, or return types.

### Q: What is upcasting and downcasting?
Upcasting: assigning a subclass reference to a superclass reference (implicit, no cast). Downcasting: assigning a superclass reference to a subclass reference (explicit cast required; use instanceof to avoid ClassCastException).

### Q: What is encapsulation and how is it typically implemented?
Encapsulation restricts direct access to an object's state. Make fields private and expose them through public getters and setters (or other methods).
