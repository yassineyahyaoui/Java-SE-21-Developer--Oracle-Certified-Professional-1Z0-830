# Module 02 -- Introduction to Java and Environment Setup

### Q: How do you print text without a newline in Java?
Use `System.out.print("text");`. It writes the string to the console and does not add a newline after it.

### Q: How do you print text with a newline in Java?
Use `System.out.println("text");`. It prints the string to the console and inserts a newline after it.

### Q: How do you format output with placeholders in Java?
Use `System.out.printf(format, args)`. Common format specifiers: `%d` for integers, `%s` for strings, `%n` for a platform-independent newline (e.g. `printf("Value: %d%n", x)`).

### Q: How do you read an integer from user input with Scanner?
Create a `Scanner` (e.g. `Scanner sc = new Scanner(System.in);`) and call `int n = sc.nextInt();` to read the next token as an int.

### Q: What is the difference between Scanner next(), nextLine(), and nextInt()?
`next()` reads the next token (stops at whitespace). `nextLine()` reads the rest of the current line including spaces. `nextInt()` reads the next token and parses it as an int.

### Q: How do you write a single-line comment in Java?
Use `//` — everything from `//` to the end of the line is a comment.

### Q: How do you write a multi-line comment in Java?
Use `/* ... */` — everything between the delimiters is a comment and can span multiple lines.

### Q: How do you write a Javadoc comment in Java?
Use `/** ... */` (two asterisks). Javadoc comments document classes, methods, and parameters and can be processed by the `javadoc` tool to generate API documentation.

### Q: What is the JDK and when do you need it?
The JDK (Java Development Kit) is a software development environment for building Java applications. It includes the JRE, compilers (e.g. javac), debugger, and other development tools. You need the JDK to develop and run Java applications.

### Q: What is the JRE and what does it contain?
The JRE (Java Runtime Environment) is the runtime portion of Java software. It bundles the JVM and libraries needed to run applications written in Java. End users who only run Java programs need the JRE, not the full JDK.

### Q: What is the JVM and what does it do?
The JVM (Java Virtual Machine) is a virtual machine that runs Java programs. It executes bytecode: it takes .class files (bytecode) and translates them into native machine code that the host machine can run.

### Q: What is bytecode and how is it produced?
Bytecode is the intermediate, platform-independent instruction set produced when you compile Java source (.java) with the Java compiler (javac). The output is in .class files that the JVM executes.

### Q: What does "write once, run anywhere" mean in Java?
Compiled Java code (bytecode) can run on any platform that has a JVM, without recompiling the source. You can write and compile on one OS (e.g. Windows) and run the same .class files on another (e.g. Linux or Mac).

### Q: What is the relationship between JDK, JRE, and JVM?
The JDK contains the JRE and development tools. The JRE contains the JVM and libraries. So: JDK ⊃ JRE ⊃ JVM. Developers need the JDK; users who only run Java apps typically need only the JRE (which includes the JVM).

### Q: Which main tools does the JDK provide for a new developer?
The main tools are the javac compiler (compiles .java to .class), the java launcher (runs applications), and the javadoc tool (generates API documentation from Javadoc comments).

### Q: What is widening conversion in Java and is a cast required?
Widening conversion is when a value of a smaller or more restrictive type is assigned to a larger type (e.g. int to long, int to double). It is automatic and safe; no explicit cast is required.

### Q: What is narrowing conversion in Java and is a cast required?
Narrowing conversion is when a value of a larger type is assigned to a smaller type (e.g. long to int, double to int). It can lose information, so the compiler requires an explicit cast: e.g. `int i = (int) longValue;`.

### Q: In `public static void main(String[] args)`, what does each part mean?
`public` — access modifier so the JVM can call it. `static` — method belongs to the class; JVM invokes it without creating an object. `void` — no return value. `String[] args` — command-line arguments passed by the runtime.

### Q: Why must a runnable Java application have a main method with this exact signature?
The JVM looks for a method named `main` with signature `public static void main(String[] args)` to use as the application entry point. Without it, the runtime does not know where to start executing.

### Q: What are the steps from writing code to seeing output (compile and run)?
You write .java source → javac compiles it to .class (bytecode) → the JVM loads and executes the .class (translates bytecode to native code and runs it) → you see the program output (e.g. in the console).
