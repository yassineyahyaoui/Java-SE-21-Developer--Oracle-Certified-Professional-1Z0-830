# Day 16 -- OOP Programming (Part 3) — Pattern Matching

### Q: What is static polymorphism vs dynamic polymorphism in Java?
**Static polymorphism** is resolved at compile time; the classic example is **method overloading** (same method name, different parameter lists). **Dynamic polymorphism** is resolved at runtime; the classic example is **method overriding** (subclass method replaces superclass method when invoked on a subclass object via a superclass reference).

### Q: What is upcasting and is an explicit cast required?
Upcasting is assigning a subclass reference to a superclass reference (e.g. `Vehicle v = new Car();`). It is **implicit**—no cast needed. The reference type is the superclass; the object is still the subclass.

### Q: What is downcasting and when do you need it?
Downcasting is assigning a superclass reference to a subclass reference (e.g. `Car c = (Car) v;`). It requires an **explicit cast**. You should check with `instanceof` first to avoid ClassCastException at runtime: `if (v instanceof Car) { Car c = (Car) v; }`.

### Q: What happens if you downcast without checking and the object is not of the target type?
A **ClassCastException** is thrown at runtime. Not all cast errors are caught at compile time; the compiler allows the cast if the types are in the same hierarchy, but the JVM checks the actual object type at runtime.

### Q: What is encapsulation and how is it typically implemented?
Encapsulation restricts direct access to an object’s state. Typically: make fields **private** and expose them through **public** (or appropriate) **getters and setters**. Code outside the class then interacts via methods rather than direct field access.

### Q: Can an anonymous class define a constructor?
No. Anonymous classes have no name, and a constructor must have the same name as the class. You cannot declare a constructor in an anonymous class. You can use instance initializers or pass arguments to the superclass constructor when extending a class.

### Q: What is a record class and what does the compiler generate for it?
A **record** is a compact way to define immutable data carriers. You declare components in the header (e.g. `record Person(String name, int age)`). The compiler generates: a canonical constructor, accessors (e.g. `name()`, `age()`), and implementations of `equals`, `hashCode`, and `toString` based on the components.

### Q: Are record classes mutable? Can you add setter methods?
Records are **immutable** by design. Their components are final. The compiler does not generate setters, and you should not add setters that change component values. To “change” data, you create a new record instance.

### Q: Can a record have a no-arg (parameterless) constructor?
You cannot define a normal no-arg constructor that does not delegate. You can use a compact constructor that delegates to the canonical one with default values (e.g. `this("", 0)`), effectively giving a parameterless way to construct, but the canonical constructor always has all components. A standalone no-arg constructor that does not call another constructor is not allowed.

### Q: What is a compact (canonical) constructor in a record?
A compact constructor has no parameter list: just the record name and a block, e.g. `public Person { if (age < 0) throw ...; }`. It is used to validate or normalize the components. It runs after the implicit assignment of parameters to fields; you can reassign the implicit fields in the body.

### Q: Can a record extend another class or be extended?
A record **cannot** extend any class (its direct superclass is always `Record`). A record is **implicitly final**, so it cannot be extended. A record **can** implement interfaces.

### Q: Can you use instance fields (non-component fields) in a record?
The only instance “state” is the components in the header. You cannot declare additional instance fields that are not part of the record components. You can have **static** fields. Nested record classes are implicitly static.

### Q: What is the `var` keyword and where can it be used?
`var` enables **local variable type inference**: the compiler infers the type from the initializer. It can be used only for **local variables** (inside methods, constructors, or blocks). The variable must be initialized when declared.

### Q: Where can you NOT use `var`?
You cannot use `var` for: **fields** (instance or static), **method parameters**, or **method return type**. Using `var` there causes a compile error.

### Q: Can you declare `var x;` without initializing?
No. A variable declared with `var` must be initialized in the same statement so the compiler can infer the type. Otherwise you get a compile error.

### Q: Can you assign `null` to a `var` variable?
Not by itself. `var x = null;` is a compile error because the type cannot be inferred from `null`. You can use a cast or a typed null, e.g. `var list = (List<String>) null;` (type is then inferred as List<String>).

### Q: If a method parameter is of superclass type, can you pass a subclass object?
Yes. That is polymorphism. For example, if a method takes `Vehicle v`, you can pass a `Car` or `Motorcycle` instance. The overridden method of the actual object type is invoked at runtime.
