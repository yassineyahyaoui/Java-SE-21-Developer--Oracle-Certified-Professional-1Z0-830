# Day 40 -- Mock Exam #1

### Q: Who developed Java and at which company?
James Gosling, Mike Sheridan, and Patrick Norton at Sun Microsystems in the early 1990s. The language was initially called Oak and later repurposed for the internet.

### Q: What is the JVM responsible for?
The JVM executes Java bytecode (produced by the compiler). It does not compile source to machine code directly; it runs bytecode and provides platform independence (write once, run anywhere).

### Q: Why does redeclaring a local variable in a nested block cause a compile error?
Java does not allow redeclaring a variable in the same or nested scope. If `int x` exists in main, an inner block cannot declare `int x = 20`; use assignment `x = 20` instead.

### Q: With `x = 5`, what is the value of x after `(x > 2) || (++x < 10)`?
x stays 5. The first condition is true, so the `||` short-circuits and `++x` is never evaluated. With non-short-circuit `|`, `++x` would run and x would be 6.

### Q: When does a switch statement fail to compile due to case values?
When the same case value appears twice (e.g. `case 2:` and `case 3-1:` both mean 2). Duplicate case constants are a compile-time error.

### Q: In a jagged array, what happens when you access an index that doesn’t exist in that row?
You get a runtime IndexOutOfBoundsException, not a compile error. Java allows rows of different lengths; the error occurs when you access, e.g., the third element of a row that has only two.

### Q: Does the for-each loop variable modify the original array?
No. The loop variable is a copy of the element, not a reference. Assigning to it (e.g. `num *= 2`) does not change the array.

### Q: For overloaded methods, how does Java choose between an exact match and a varargs match?
Exact match is preferred. For `print(5, 10)`, the two-int version is chosen over the varargs `print(int... nums)` because both arguments match int exactly. Varargs is used when no exact match exists.

### Q: When can overloaded method calls be ambiguous and not compile?
When more than one method is applicable via widening and both are equally specific. E.g. `print(5, 10)` with `print(int, double)` and `print(double, int)`—both need one widening conversion, so the compiler cannot choose.

### Q: Which operators can be used with boolean in Java?
Equality `==`, `!=`; logical AND `&&`, OR `||`, complement `!`. Not allowed: `++`, `+=`, `-`, `>=`, etc.

### Q: What are the rules for static import?
Only static members (fields and methods) of another class can be statically imported. The imported member must be static; private methods are not accessible from another class anyway.

### Q: In a constructor, what does `this.x` refer to if the parameter is also named x and you haven’t assigned it yet?
`this.x` refers to the (static or instance) field of the class, not the parameter. So before assigning the parameter to the field, printing `this.x` shows the field’s default or initial value.

### Q: For a sealed class, what must each permitted subclass declare?
Each permitted subclass must be declared as `final`, `sealed`, or `non-sealed`. If it’s sealed, it must have its own `permits` clause.

### Q: Why does `record class Student` not compile?
A record is declared with `record Name(...)` only, not `record class`. The `class` keyword after `record` causes a compile error.

### Q: When creating a Cat that extends Animal, which constructor runs first?
The parent (Animal) constructor runs first, then the child (Cat) constructor. The compiler inserts a `super()` call if you don’t; constructors chain from the top down.

### Q: Can interfaces have default and static methods? Can static interface methods be overridden?
Interfaces can have default methods (Java 8) and private static methods (Java 9). Static methods in an interface belong to the interface and cannot be overridden by implementing classes.

### Q: If a thread in WAITING or TIMED_WAITING is interrupted, what happens?
Interrupting that thread causes an InterruptedException. Code that calls `wait()` or similar must handle or declare InterruptedException.

### Q: With ZonedDateTime and DST end (e.g. Chicago Nov 7, 2021), adding one hour during the repeated 1–2 am can give the same clock hour but different zone offset. What does equals() compare?
ZonedDateTime’s equals() considers both the instant and the zone. So “1:30 DST + 1 hour” may still be 1:30 but in standard time; the offset change can make equals() false even when the local hour is the same.

### Q: What do Stream’s allMatch, anyMatch, and noneMatch return? What does findFirst return?
They return boolean (allMatch, anyMatch, noneMatch) and Optional&lt;T&gt; (findFirst). findFirst returns an Optional containing the first element, or empty if the stream is empty.

### Q: How does Integer caching affect == for boxed values?
For values in the range -128 to 127, Integer uses cached instances. So `Integer a = 100; Integer b = 100;` can give `a == b` true. Outside that range, new objects are created and `==` is false; use equals() for value comparison.

### Q: What does Arrays.asList(...) return and can you add to it?
It returns a fixed-size list backed by the array. Adding or removing elements throws UnsupportedOperationException. It’s a view of the array, not a full ArrayList.

### Q: Do intermediate or terminal stream operations produce a new stream?
Intermediate operations (e.g. filter, map, sorted) return a new stream. Terminal operations (e.g. forEach, collect, count) produce a result or side effect and close the stream.

### Q: What exception does Files.walk(path) throw if the path doesn’t exist?
NoSuchFileException (a kind of IOException) at runtime. Files.walk() does not create the directory; it traverses an existing directory tree.

### Q: How does join() affect the order in which thread output appears?
If the main thread does t1.start(), t1.join(), t2.start(), t2.join(), the main thread waits for t1 to finish before starting t2. So t1’s output always appears before t2’s (e.g. A then B).

### Q: In a switch expression, can the same constant appear in two case labels?
No. Duplicate case values in a switch expression (or statement) cause a compile error.

### Q: How does LinkedHashMap behave when created with accessOrder true?
Iteration order is access order: least recently accessed to most recently accessed. get(key) or put on an existing key counts as access and moves that entry to the end of the iteration order.

### Q: When are enum constructors invoked?
When the enum class is loaded, all constants are initialized, so the constructor runs once per constant. After that, using an enum constant does not run the constructor again.

### Q: Is reflection fully supported in GraalVM native image by default?
No. Reflection and dynamic class loading typically need extra configuration (e.g. reflection config) in native images. “Fully supported without additional configuration” is false.

### Q: What is required in a JAR manifest for an executable JAR?
The Main-Class attribute (fully qualified class name containing the main method). Other attributes (Class-Path, Manifest-Version, etc.) are optional for executability.

### Q: For a sealed interface Content with permits Story, Art, what must Story and Art be?
They must be interfaces or classes that explicitly extend/implement Content and declare themselves as final, sealed, or non-sealed. Both can be non-sealed interfaces.

### Q: In instanceof pattern matching, e.g. `if (cObj instanceof B b)`, what is the type of b in the if block?
The type of b is B. If the object is actually a subclass C of B, b still has type B inside that block; you can nest another `if (b instanceof C c)` to narrow to C and use c.

### Q: Does setting a reference parameter to null inside a method affect the caller’s reference?
No. Java is pass-by-value; the parameter is a copy of the reference. Assigning null to the parameter does not change the caller’s reference, so the caller still sees the original object (or null if that’s 
