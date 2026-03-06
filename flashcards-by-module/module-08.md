# Module 08 -- Java Object-Oriented Concept

### Q: What is OOP fundamentals: class as blueprint?

Explain OOP fundamentals: class as blueprint, object as instance with state (fields), behavior (methods), and identity; create objects with `new`

### Q: Describe JVM memory: stack (per-thread, LIFO, local vars/references, `StackOverflowError`) vs heap (shared, objects/instance vars, garbage collected, `OutOfMemoryError`)?

Describe JVM memory: stack (per-thread, LIFO, local vars/references, `StackOverflowError`) vs heap (shared, objects/instance vars, garbage collected, `OutOfMemoryError`)

### Q: How do you apply all four access modifiers and state their restrictiveness order: `private` > default (package-private) > `protected` > `public`; predict cross-package visibility?

Apply all four access modifiers and state their restrictiveness order: `private` > default (package-private) > `protected` > `public`; predict cross-package visibility

### Q: Follow Java naming conventions: class = uppercase noun, method = lowercase verb, variable = lowercase camelCase; identify valid/invalid identifiers?

Follow Java naming conventions: class = uppercase noun, method = lowercase verb, variable = lowercase camelCase; identify valid/invalid identifiers

### Q: How do you constructors (same name as class, no return type, overloadable) with `this.field = param`; explain the default no-arg constructor; override `toString()`?

Write constructors (same name as class, no return type, overloadable) with `this.field = param`; explain the default no-arg constructor; override `toString()`

### Q: Declare packages with hierarchical dot-separated names, explain source file order (`package` -> `import` -> class), and state that `java.lang` is auto-imported?

Declare packages with hierarchical dot-separated names, explain source file order (`package` -> `import` -> class), and state that `java.lang` is auto-imported

### Q: How do you use `import pkg.Class` and wildcard `import pkg.*`; resolve name conflicts between packages using fully qualified class names?

Use `import pkg.Class` and wildcard `import pkg.*`; resolve name conflicts between packages using fully qualified class names

### Q: How do you use the `static` keyword on variables (one copy per class), methods (called via class name), and blocks (run when class loads); explain why instance members cannot be used directly in a static context?

Use the `static` keyword on variables (one copy per class), methods (called via class name), and blocks (run when class loads); explain why instance members cannot be used directly in a static context

### Q: How do you `import static` statements to use static members without the class name prefix?

Write `import static` statements to use static members without the class name prefix

### Q: Describe static nested classes (access only outer static members) vs inner classes (access all outer members including private) and their different instantiation syntax?

Describe static nested classes (access only outer static members) vs inner classes (access all outer members including private) and their different instantiation syntax

### Q: What is local?

Define local inner classes inside a method block and explain that they can access effectively final local variables (JDK 8+)

### Q: What is OOP or OOP, um?

OOP or OOP, um is a method of designing and implementing software.

### Q: What is A Java object?

A Java object is a self-contained component which consists of methods and properties.

### Q: What is And here my car, the object?

And here my car, the object is the reference which holds the memory address of the car object.

### Q: What is But conversely, if the exact data size required at r...?

But conversely, if the exact data size required at runtime is unknown, or if there is a need to allocate substantial data, you're going to want to opt for heap memory.

### Q: What is You might be a little confused, but I remind you, co...?

You might be a little confused, but I remind you, confusion is the first step to enlightenment.

### Q: What is the public access modifier?

So the public access modifier is the least restrictive, as you might imagine, allowing access from any part of the code within the same class.

### Q: What is in direct contrast, private?

So in direct contrast, private is the most restrictive access level.

### Q: What is And this will give the message this?

And this will give the message this is the public method.

### Q: What is Java naming convention?

Java naming convention is a rule to follow how to name your identifiers like class, variable, method, etc.

### Q: What is Camel casing?

Camel casing is a naming convention in which the first letter of the second word in a compound word is capitalized.

### Q: What is Because public is not the same as public in Java bec...?

Because public is not the same as public in Java because Java is a case sensitive language.

### Q: What is And that, my friends?

And that, my friends, is the constructor.

### Q: What is perhaps, as this name suggests, a constructor?

Now, perhaps, as this name suggests, a constructor is a structure we encounter when creating objects from a class.

### Q: What is In Java, a constructor?

In Java, a constructor is a special method within a class that is automatically called when an object of that class is created.

### Q: What is The second?

The second is the default constructor.

### Q: What is here the animals?

So here the animals is a top level package.

### Q: What is The first one?

The first one is the built in package.

### Q: What is The second one?

The second one is the user defined package.

### Q: What is And that Oak?

And that Oak is a parent package and Academy is a child package.

### Q: What is the static method?

Now, the static method is a method which belongs to the class and not to the object, right.

### Q: What is Static block?

Static block is a block of statement inside a Java class that will be executed when a class is first loaded into the Java virtual machine, and we will also cover nested class and interface in the next slides.

### Q: What is We always created these methods static because the m...?

We always created these methods static because the main method is a static method, and inside a static method we can only call static variables or static methods directly.

### Q: What is Well, as you can see, we can also reach methods in t...?

Well, as you can see, we can also reach methods in the car class, but there is a little bit of a difference.

### Q: What is There you see the output?

There you see the output is the same.
