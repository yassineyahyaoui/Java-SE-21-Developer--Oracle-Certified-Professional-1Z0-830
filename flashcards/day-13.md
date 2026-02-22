# Day 13 -- OOP Concepts (Part 2)

### Q: What is the required order of elements in a Java source file?
Package declaration (if present) first, then import statements, then the class declaration. Only one package declaration per file. The public class (if any) must match the filename.

### Q: Which package is automatically imported in every Java program?
java.lang. Classes such as String, System, and Math are in java.lang and do not require an explicit import.

### Q: What is the difference between importing a single class and using a wildcard import?
Single: `import pkg.ClassName;` — only that class is available. Wildcard: `import pkg.*;` — all classes (and interfaces) in that package are available; classes in subpackages are not included.

### Q: How do you resolve a name conflict when two classes with the same name are from different packages?
Use the fully qualified name at the point of use, e.g. `packageone.Sum s1 = new packageone.Sum();` and `packagetwo.Sum s2 = new packagetwo.Sum();`. Avoid importing both with wildcards or both same-named classes; that causes an “ambiguous type” error.

### Q: Why can’t you use an instance variable or call an instance method directly from a static method?
Static members belong to the class and exist without an instance. Instance members belong to each object. From a static context there is no “this” object, so you must either make the member static or create an object and use it (e.g. `obj.instanceMethod()`).

### Q: What happens if a static method uses a non-static variable?
You get a compilation error. To fix it, either make the variable static or access it through an object of the class (create an instance and use that instance’s variable).

### Q: How do you declare and use a static variable or static method?
Declare with the `static` keyword (e.g. `static int count;`, `static void show() {}`). Access by class name: `ClassName.variable` or `ClassName.method()`. No object is required; one copy is shared for the class.

### Q: What is a static block and when does it run?
A static block is a block of code in a class preceded by the `static` keyword. It runs when the class is first loaded by the JVM, before any instance is created or static method is called.

### Q: What is import static and how do you use it?
import static lets you import static members (fields and methods) so you can use them without the class name. Example: `import static java.lang.Math.pow;` then call `pow(2, 3)` instead of `Math.pow(2, 3)`. Wildcard: `import static pkg.Class.*;`.

### Q: What is the difference between a static nested class and an inner (non-static nested) class?
Static nested class: declared with `static`; instantiated as `Outer.StaticNested obj = new Outer.StaticNested();`; can only access static members of the outer class. Inner class: not static; instantiated as `Outer.Inner inner = outer.new Inner();`; can access both static and instance members of the outer class.

### Q: Can a static nested class access instance (non-static) members of the outer class?
No. A static nested class can only access static members of the outer class. Access modifiers do not change this; even public instance fields are not directly accessible from the static nested class.

### Q: How do you create an instance of a static nested class vs an inner class?
Static nested: `Outer.StaticNested obj = new Outer.StaticNested();` (no outer instance needed). Inner: you must have an outer instance: `Outer outer = new Outer();` then `Outer.Inner inner = outer.new Inner();`.

### Q: What is a local inner class and where can it be defined?
A class defined inside a block (usually a method body, or a block like a loop or if). It is not a member of the enclosing class; it belongs to the block. It can be marked final or abstract but cannot have access modifiers.

### Q: Can a local inner class be instantiated from outside the block where it is defined?
No. A local inner class can only be instantiated and used within the same block (e.g. method) where it is defined. It is not visible outside that block.

### Q: What rule do local inner classes follow regarding local variables of the enclosing block?
From Java 8 onward, they can access local variables that are effectively final (never reassigned after initialization). Before Java 8, only final local variables could be accessed. This is the “effectively final” rule for local classes and lambdas.

### Q: Can a local inner class access the parameters of the enclosing method?
Yes (Java 8+). A local class defined in a method can access that method’s parameters, as long as they are effectively final.
