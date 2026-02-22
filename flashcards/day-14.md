# Day 14 -- OOP Programming (Part 1)

### Q: How do you create a subclass in Java and what keyword is used?
Use the `extends` keyword after the class name: `class MountainBike extends Bicycle`. Each class has exactly one direct superclass (single inheritance).

### Q: Are constructors inherited by subclasses?
No. Constructors are not members, so they are not inherited. The superclass constructor can be invoked from the subclass (e.g. with `super()`), but the subclass does not “inherit” it.

### Q: What visibility do inherited members have? When does a subclass inherit public, protected, package-private, and private?
A subclass always inherits **public** and **protected** members regardless of package. It inherits **package-private** (default) members only if in the same package as the superclass. It **never** inherits **private** members (though it can use public/protected accessors for private superclass fields).

### Q: What is the root of the Java class hierarchy and does it have a superclass?
`Object` (in `java.lang`) is the root. Every class without an explicit superclass implicitly extends `Object`. `Object` has no superclass.

### Q: What are single, multi-level, and hierarchical inheritance?
**Single**: one class extends another (e.g. RoadBike extends Bicycle). **Multi-level**: a chain (e.g. Vehicle → Bicycle → RoadBike); the bottom class can use inherited behavior from all levels but cannot directly reference “grandparent” members. **Hierarchical**: one superclass has multiple subclasses (e.g. Bicycle extended by MountainBike, RoadBike, TandemBike).

### Q: How do you declare a sealed class and what does `permits` do?
Use `sealed` on the class and a `permits` clause listing allowed subclasses: `public sealed class Animal permits Dog, Cat, Bird { }`. Only the permitted classes may extend the sealed class.

### Q: What must a direct subclass of a sealed class be declared as?
Each permitted subclass must be declared as **final**, **sealed**, or **non-sealed**. If you don’t, you get a compile error. This keeps the hierarchy under control.

### Q: What is method overriding and what must match between superclass and subclass method?
Overriding is defining in a subclass a method with the **same name, same parameters, and same return type** as in the superclass. The subclass version replaces the superclass version for that subclass.

### Q: Can the overriding method have a more restrictive access modifier than the overridden method?
No. You cannot reduce visibility. If the superclass method is `public`, the overriding method must be `public`. You can widen (e.g. superclass `protected` → subclass `public`) but not narrow (e.g. `public` → `private` causes “cannot reduce the visibility” error).

### Q: What is the `this` keyword used for?
`this` refers to the current instance. Uses: refer to instance variables (e.g. `this.x = x` when parameter shadows the field), call current class methods, call another constructor of the same class (`this(args)`), pass as argument or return the current instance.

### Q: What is the `super` keyword used for?
`super` refers to the superclass. Uses: access superclass fields (`super.field`), call superclass methods (`super.method()`), and invoke superclass constructor (`super()` or `super(args)`). The super constructor call must be the first statement in a constructor if present.

### Q: Where can `this()` (constructor call) be used and what rule must you follow?
Only inside a constructor body, and it must be the first statement. It cannot be used in ordinary methods. Avoid recursive constructor calls (e.g. default calling parameterized and parameterized calling default).

### Q: Does Java support multiple inheritance of classes?
No. A class can extend only one class. Multiple and hybrid inheritance are possible only with **interfaces**, not with classes.

### Q: If a subclass declares a field with the same name as a superclass field, what happens?
The subclass field **hides** the superclass field (not override—fields are not polymorphic). This is allowed but generally discouraged; use different names or access via `super` when you need the superclass field.

### Q: What can you do with inherited methods in a subclass?
Use them as-is, override them (same signature, replace behavior), declare new methods. For static methods, a same-signature method in the subclass **hides** (does not override) the superclass static method.
