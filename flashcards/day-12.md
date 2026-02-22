# Day 12 -- OOP Concepts (Part 1)

### Q: What is a class and what is an object in Java?
A class is a blueprint or template that defines state (fields) and behavior (methods). An object is an instance of a class—a concrete entity created in memory with its own state, behavior, and identity.

### Q: What are the three characteristics of an object?
State (the data/attributes of the object), behavior (actions the object can perform, implemented by methods), and identity (used internally by the JVM to uniquely identify each object; not directly visible to the programmer).

### Q: How do you create an object in Java?
Use the `new` keyword: e.g. `Car myCar = new Car();`. The reference variable (e.g. `myCar`) holds the address of the object; the actual object is created on the heap.

### Q: What is stored on the stack vs the heap in the JVM?
Stack: per-thread, LIFO; holds local variables, method call frames, primitive values, and references to objects. Heap: shared by the application; holds objects and instance variables; managed by the garbage collector.

### Q: Where are local variables, method calls, and object references stored? Where are objects and instance variables stored?
Local variables, method calls, and references to objects are stored on the stack. Objects and instance variables live on the heap; the stack holds only the reference (address) to the object.

### Q: What is the order of restrictiveness of the four access modifiers, from most to least restrictive?
Private (most restrictive), then default (package-private), then protected, then public (least restrictive). Private allows only the declaring class; public allows access from anywhere.

### Q: From a class in a different package, which access modifier(s) can you use to access a member?
Only public. Default and protected members are not accessible from a different package (unless it’s a subclass for protected). Private is never visible outside the declaring class.

### Q: Where can a default (package-private) member be accessed?
Only from the same package—same class and other classes in that package. Not from subclasses or classes in other packages.

### Q: Where can a protected member be accessed?
From the same class, other classes in the same package, and from subclasses (even in another package). Not from unrelated classes in a different package.

### Q: What are Java naming conventions for classes, methods, and variables?
Class names: start with an uppercase letter, use nouns (e.g. String, Car). Method names: start with lowercase, use verbs (e.g. start, getValue). Variable names: start with lowercase, camelCase (e.g. firstName, year).

### Q: What defines a constructor and how is it different from a normal method?
A constructor has the same name as the class and has no return type (not even void). It is invoked when an object is created with `new` and is used to initialize the object’s state.

### Q: What is the default constructor and when does Java provide it?
If a class does not define any constructors, the compiler supplies a default no-arg constructor that takes no parameters and initializes fields to default values. If you define any constructor, the default constructor is not provided.

### Q: Can a class have multiple constructors?
Yes. Constructors can be overloaded: same name as the class, different parameter lists. The appropriate constructor is chosen based on the arguments passed to `new`.

### Q: What does toString() do and when is it used?
toString() returns a string representation of an object. If you override it in your class, printing an object (e.g. `System.out.println(person)`) or using it in string concatenation calls your toString(). Without an override, the default implementation prints something like class name and object identity (e.g. package.ClassName@hashcode).

### Q: Which characters are valid at the start of a class or variable name?
Letters, underscore (_), and dollar sign ($). Digits and other special characters (e.g. %, @, &) are not allowed at the start. Java is case-sensitive, so `Public` is valid even though `public` is a keyword.

### Q: Why might you use private for fields and public for constructors?
Private fields encapsulate data so other classes cannot change it directly. Public constructors allow objects to be created from other classes; constructors are typically public so that code outside the class can instantiate the class.
