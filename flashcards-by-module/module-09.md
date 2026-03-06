# Module 09 -- Java Object-Oriented Programming

### Q: Implement inheritance with `extends` and explain single, multi-level, and hierarchical inheritance; state that constructors are not inherited but can be invoked with `super()`?

Implement inheritance with `extends` and explain single, multi-level, and hierarchical inheritance; state that constructors are not inherited but can be invoked with `super()`

### Q: What is visibility of inherited members: `public`/`protected` always?

Explain visibility of inherited members: `public`/`protected` always, package-private only in same package, `private` never; `Object` is the root of every class hierarchy

### Q: Declare sealed classes with `sealed` + `permits` and state that subclasses must be `final`, `sealed`, or `non-sealed`?

Declare sealed classes with `sealed` + `permits` and state that subclasses must be `final`, `sealed`, or `non-sealed`

### Q: Override methods correctly: same name/parameters/return type, access modifier cannot be more restrictive than the superclass method?

Override methods correctly: same name/parameters/return type, access modifier cannot be more restrictive than the superclass method

### Q: How do you use `this` to reference the current instance (fields, methods, constructor) and `super` to access superclass members (fields, methods, constructor)?

Use `this` to reference the current instance (fields, methods, constructor) and `super` to access superclass members (fields, methods, constructor)

### Q: How do you use `super.field` to access a shadowed parent variable, `super.method()` to call a parent method, and `super()` to invoke a parent constructor; combine `this` and `super` in constructor chaining?

Use `super.field` to access a shadowed parent variable, `super.method()` to call a parent method, and `super()` to invoke a parent constructor; combine `this` and `super` in constructor chaining

### Q: How do you apply the `final` keyword: `final` class cannot be extended, `final` method cannot be overridden, `final` variable cannot be reassigned (constant)?

Apply the `final` keyword: `final` class cannot be extended, `final` method cannot be overridden, `final` variable cannot be reassigned (constant)

### Q: Declare abstract classes and methods; explain that abstract classes cannot be instantiated but can have constructors and non-abstract methods; state that abstract methods cannot be `final`, `private`, or `static`?

Declare abstract classes and methods; explain that abstract classes cannot be instantiated but can have constructors and non-abstract methods; state that abstract methods cannot be `final`, `private`, or `static`

### Q: What is interfaces?

Define interfaces with `implements`; explain that interface variables are implicitly `public static final` and methods are implicitly `public abstract`; write `default` and `static` methods with a body (Java 8+)

### Q: Implement multiple interfaces in a single class and combine `extends` (one class) with `implements` (multiple interfaces)?

Implement multiple interfaces in a single class and combine `extends` (one class) with `implements` (multiple interfaces)

### Q: What is static polymorphism (method overloading)?

Explain static polymorphism (method overloading) and dynamic polymorphism (method overriding with superclass reference to subclass object)

### Q: How do you implicit upcasting (`Vehicle v = new Car()`) and explicit downcasting with `instanceof` check to avoid `ClassCastException`?

Perform implicit upcasting (`Vehicle v = new Car()`) and explicit downcasting with `instanceof` check to avoid `ClassCastException`

### Q: How do you apply encapsulation: private fields with public `getXxx`/`setXxx` getters and setters; design read-only or write-only access patterns?

Apply encapsulation: private fields with public `getXxx`/`setXxx` getters and setters; design read-only or write-only access patterns

### Q: How do you anonymous classes (`new Interface() { ... }`) for one-off implementations; state that they cannot define constructors and require effectively final local variables?

Write anonymous classes (`new Interface() { ... }`) for one-off implementations; state that they cannot define constructors and require effectively final local variables

### Q: Declare record classes (`record Name(components)`) and use their generated accessors, `equals`, `hashCode`, `toString`; write compact canonical constructors for validation; list what records can/cannot have?

Declare record classes (`record Name(components)`) and use their generated accessors, `equals`, `hashCode`, `toString`; write compact canonical constructors for validation; list what records can/cannot have

### Q: How do you use `var` for local variable type inference (Java 10) and state its limitations: not for fields, parameters, return types; must be initialized; cannot assign `null` alone; cannot use with lambda or array brackets?

Use `var` for local variable type inference (Java 10) and state its limitations: not for fields, parameters, return types; must be initialized; cannot assign `null` alone; cannot use with lambda or array brackets

### Q: What is it's used when we have an?

So it's used when we have an is a relationship between objects.

### Q: What is for example a mountain bike?

So for example a mountain bike is a bicycle, a road bike is a bicycle, a tandem bike is a bicycle.

### Q: What is That's why object?

That's why object is the exception.

### Q: What is at the bottom of the hierarchy object?

Now, at the bottom of the hierarchy object is the most general of all these classes.

### Q: What is what you're looking at on the screen here?

So what you're looking at on the screen here is the class bicycle serves as a base class for the derived class mountain bike, road bike and tandem bike.

### Q: What is in the example on the screen the vehicle class?

Now in the example on the screen the vehicle class is the superclass.

### Q: What is Well, that?

Well, that is a good question.

### Q: What is naturally in this case, the animal's class?

So naturally in this case, the animal's class is a sealed class and only the dog, the cat, and the bird classes can then inherit from that animals class.

### Q: What is Overriding what we'll do here?

Overriding what we'll do here is a let's create a main test class that we'll name override test in the same package.

### Q: What is The reason for this is that there?

The reason for this is that there is a ranking among the access modifiers.

### Q: What is if you notice this car now references the car which?

Now if you notice this car now references the car which is the instance of this class.

### Q: What is The year here also?

The year here also refers to year which is also an instance of this class and the car and the year to the right of the equal sign refer to the variables that are parameters.

### Q: What is You see that the result?

You see that the result is the same.

### Q: What is In fact, this?

In fact, this is the method calling that we've done so far that you may be familiar with.

### Q: What is And that?

And that is the parameter less constructor.

### Q: What is in this video why don't we just talk about the super...?

So in this video why don't we just talk about the super keyword and the super call now, in fact, it actually wouldn't be wrong to say the keyword super and this or logically similar to each other, but the difference is that the this keyword refers to the class it is in, while the super keyword refers to the super class it inherits.

### Q: What is the super keyword in Java?

So the super keyword in Java is a reference variable which is used to refer to a parent class object.

### Q: What is what you're looking at?

So what you're looking at is the true and the false are printed on the console.

### Q: What is And this type?

And this type is the instance variable of this class.
