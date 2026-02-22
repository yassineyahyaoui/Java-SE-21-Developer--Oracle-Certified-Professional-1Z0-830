# Day 2 -- Java Environment (finish)

### Q: What is widening conversion in Java and is a cast required?
Widening conversion is when a value of a smaller or more restrictive type is assigned to a larger type (e.g. int to long, int to double). It is automatic and safe; no explicit cast is required.

### Q: What is narrowing conversion in Java and is a cast required?
Narrowing conversion is when a value of a larger type is assigned to a smaller type (e.g. long to int, double to int). It can lose information, so the compiler requires an explicit cast: e.g. `int i = (int) longValue;`.

### Q: Why can narrowing cause data loss? Give an example.
The target type has fewer bits or a smaller range. Example: assigning a long or double to an int can truncate or lose precision (e.g. `(int) 9_000_000_000L` or `(int) 3.9` may not represent the original value).

### Q: How do you fix a compiler error when assigning a larger numeric type to a smaller one?
Use an explicit cast to the target type, e.g. `int x = (int) someLong;` or `int y = (int) someDouble;`. This tells the compiler you accept the possible data loss.

### Q: How do you create a new Java project with JDK 21 in IntelliJ IDEA?
In IntelliJ: File → New → Project (or New Project from welcome). Select Java, set project name and location, choose build system (e.g. IntelliJ), then in the JDK dropdown select JDK 21 (or Add JDK → point to your JDK 21 installation). Click Create.

### Q: Where do you put Java source files in an IntelliJ Java project?
Java source files (.java) go inside the `src` folder (or in packages you create under `src`). By convention, package structure under `src` mirrors the package names.

### Q: What are the steps from writing code to seeing output (compile and run)?
You write .java source → javac compiles it to .class (bytecode) → the JVM loads and executes the .class (translates bytecode to native code and runs it) → you see the program output (e.g. in the console).

### Q: What does the javac compiler produce from a .java file?
The javac compiler reads .java source and produces .class file(s) containing bytecode—platform-independent instructions that the JVM can execute.

### Q: What does the JVM do with a .class file?
The JVM loads the .class file, interprets (or JIT-compiles) the bytecode into native machine code for the current platform, and runs it. Library code is also executed by the JVM as needed.

### Q: In `public static void main(String[] args)`, what does `public` mean?
`public` is an access modifier: the main method is visible and callable by the JVM from outside the class, which is required for the runtime to use it as the entry point.

### Q: In `public static void main(String[] args)`, what does `static` mean?
`static` means the method belongs to the class, not to an instance. The JVM can invoke main without creating an object of the class, which is why main must be static.

### Q: In `public static void main(String[] args)`, what does `void` mean?
`void` means the method does not return a value. The main method has no return type; when it finishes, the program exits (unless other non-daemon threads are running).

### Q: In `public static void main(String[] args)`, what is `String[] args`?
`String[] args` is the single parameter: an array of strings. The runtime passes command-line arguments to your application through this array (e.g. `java MyApp arg1 arg2` puts "arg1" and "arg2" in args).

### Q: Can the order of `public` and `static` be changed in the main method signature?
Yes. `public static void main(String[] args)` and `static public void main(String[] args)` are both valid. The convention is `public static`.

### Q: Why must a runnable Java application have a main method with this exact signature?
The JVM looks for a method named `main` with signature `public static void main(String[] args)` to use as the application entry point. Without it, the runtime does not know where to start executing.

### Q: How do you print "Hello World" to the console in Java?
Inside the main method, use `System.out.println("Hello World");`. This uses the `println` method of the `out` object (PrintStream) of the `System` class to print the string and then a newline.

### Q: What is the role of the main method in a Java application?
The main method is the entry point: when you run the program, the JVM calls this method first, and it typically invokes the rest of the logic (other methods and classes) of your application.
