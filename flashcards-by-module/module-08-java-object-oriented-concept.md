# Module 08 -- Java Object-Oriented Concept

### Q: What is a class and what is an object in Java?
A class is a blueprint that defines state (fields) and behavior (methods). An object is an instance of a class—a concrete entity created in memory with its own state and behavior.

### Q: What is stored on the stack vs the heap?
Stack: local variables, method call frames, primitive values, and references to objects. Heap: objects and instance variables; managed by the garbage collector.

### Q: What is the order of the four access modifiers from most to least restrictive?
private (most), then default (package-private), then protected, then public (least). Only public is accessible from a different package (unless subclass for protected).

### Q: Where can a protected member be accessed?
From the same class, same package, and from subclasses (even in another package). Not from unrelated classes in a different package.

### Q: What defines a constructor and how is it different from a method?
A constructor has the same name as the class and no return type (not even void). It is invoked with `new` and initializes the object. Methods have a return type and are called on objects or the class.

### Q: When does Java provide a default constructor?
Only if the class does not define any constructors. If you define any constructor, the default no-arg constructor is not provided.

### Q: Why can't you use an instance variable or call an instance method from a static method?
Static members belong to the class; instance members belong to each object. From a static context there is no "this" object, so you must create an instance or use static members.

### Q: What is the difference between a static nested class and an inner (non-static) class?
Static nested: declared with static; no outer instance needed to create it; can only access static members of the outer class. Inner: not static; needs an outer instance (`outer.new Inner()`); can access instance and static members of the outer class.

### Q: What is a local inner class?
A class defined inside a method or block. It is only visible and instantiable within that block. It can access effectively final local variables of the enclosing scope.
