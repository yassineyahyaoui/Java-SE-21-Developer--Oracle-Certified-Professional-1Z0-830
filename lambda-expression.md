# Java SE 21 — Lambda expressions and related topics

Study notes merged from the course module transcripts (Section overview through Enhanced switch). Exam-oriented: definitions, rules, APIs, and concise examples.

---

## Module roadmap

This section of the course covers, in order:

1. **Marker and functional interfaces** — vocabulary for lambdas.
2. **Lambda expressions** — syntax and replacing verbose anonymous classes.
3. **`Predicate`** — a standard functional interface for boolean tests.
4. **Method references** — shorthand when a lambda only forwards to one method.
5. **Console-style practice** (in the videos) — applying predicates and lambdas.
6. **Switch expressions (enhanced `switch`)** — expressions, `yield`, pattern matching, `enum` exhaustiveness (Java 12–21 evolution as presented in the course).

> **Streams:** The module demos use **`Collection.removeIf`** and **`Iterable.forEach`** with lambdas/predicates. Those are **Collection / Iterator** APIs, not the Stream API (`stream()`). Stream API is a separate topic.

---

## Functional interfaces

### Definition (SAM)

A **functional interface** is an interface that has **exactly one abstract method** (Single Abstract Method, **SAM**).

- **`abstract`** on interface methods is **optional**: interface methods without a body are abstract by default.
- The interface **may** declare **`default`** and **`static`** methods; they do **not** count toward the “one abstract method” limit.

### `@FunctionalInterface`

Annotate an interface with **`@FunctionalInterface`** (`java.lang`) to:

- **Document** intent: “this is meant to be implemented by a lambda.”
- **Enforce** the contract at compile time: if you add a second abstract method, the compiler reports an error.

The annotation is **not required** for the type to be a functional interface in the language sense—only the single abstract method rule matters for assignment compatibility with lambdas.

### Example from the JDK

**`Runnable`** (`java.lang.Runnable`): one abstract method **`void run()`**. It is a functional interface (whether or not annotated in your source, the JDK type is defined accordingly).

```java
Runnable r = () -> System.out.println("run");
```

### Functional interfaces and Java 8+

Functional interfaces, **lambda expressions**, and **method references** were introduced together in **Java 8** to support a more functional style: clearer, shorter code when behavior is passed as data.

---

## Marker interfaces

### Definition

A **marker interface** is an interface with **no methods and no fields** (empty). Implementing it **marks** the class for frameworks or the JVM; behavior comes from **other code** that checks `instanceof` the marker.

### Examples (from the course)

| Interface       | Package    | Role (high level)                          |
|----------------|------------|---------------------------------------------|
| `Cloneable`    | `java.lang` | Marks objects eligible for cloning protocol |
| `Serializable` | `java.io`   | Marks objects for serialization             |
| `Remote`       | `java.rmi`  | Marks types for RMI                         |

**`Serializable`:** Without implementing `Serializable`, a class is not treated as serializable in the normal serialization API—the marker participates in **serialization eligibility**, not by defining methods you call on the interface.

### Quick contrast

| Kind               | Abstract methods | Typical use                          |
|--------------------|------------------|--------------------------------------|
| **Functional**     | Exactly one      | Lambdas / method references target   |
| **Marker**         | None             | Metadata / capability tagging        |

---

## Lambda expressions

### Why lambdas exist

- **Anonymous classes** are useful but **verbose**, especially when the type has **only one method** to implement.
- You often want to **pass behavior** as an argument (e.g. callbacks, event handlers, strategies). Lambdas treat **“code as data”**: a compact implementation of a **functional interface**.

### Syntax (three parts)

1. **Parameter list** — `(a, b)` or `()`; types can often be inferred.
2. **Arrow token** — **`->`**
3. **Body** — a **single expression** or a **block** `{ ... }`

```java
// Expression body: no braces, no "return" for a value lambda
java.util.function.Function<String, Integer> len = s -> s.length();

// Block body: braces; use "return" if the SAM returns a value
java.util.function.Function<String, Integer> len2 = s -> {
    return s.length();
};
```

### Relationship to functional interfaces

A lambda **implements** the single abstract method of a **target type** that is a functional interface (or compatible SAM type). The compiler checks parameter count/types and return compatibility.

**Parameter names in the lambda** are **local** to the lambda; they need **not** match the parameter names in the interface method—only **types and order** matter.

### Anonymous class vs lambda (course pattern)

**Functional interface:**

```java
@FunctionalInterface
public interface Animals {
    void show(String animal, int speed);
}
```

**Anonymous inner class** (valid, verbose):

```java
Animals animal = new Animals() {
    @Override
    public void show(String animal, int speed) {
        System.out.println(animal + " can reach speeds of " + speed + " kilometers per hour");
    }
};
animal.show("cheetah", 90);
```

**Lambda** (same behavior):

```java
Animals animal = (a, s) -> {
    System.out.println(a + " can reach speeds of " + s + " kilometers per hour");
};
animal.show("cheetah", 90);
```

**Notes:**

- You **cannot** instantiate an interface with `new Animals()` without `{}` or a lambda—**interfaces are not constructed** directly.
- **`@FunctionalInterface`** on `Animals` is recommended for clarity and compile-time checking; omission does not change SAM status if there is still only one abstract method.

---

## `Predicate<T>` (`java.util.function`)

### Role

**`Predicate<T>`** is a **functional interface** in **`java.util.function`**. It models a **boolean test** on an input of type **`T`**.

- **Single abstract method:** **`boolean test(T t)`**
- **Default methods:** **`and`**, **`or`**, **`negate`** — combine or invert predicates without extra classes.

The course also mentions use in **testing** code at a high level; for the exam, focus on **typing**, **`test`**, and **composition**.

### Basic usage

```java
Predicate<Integer> lessThan10 = t -> t < 10;
lessThan10.test(5);   // true
lessThan10.test(20);  // false
```

### `String` equality and case sensitivity

```java
Predicate<String> isJava = s -> s.equals("Java");
isJava.test("Java");  // true
isJava.test("java");  // false — String equality is case-sensitive
```

### Chaining: `and` / `or`

```java
Predicate<Integer> p1 = i -> i < 10;
Predicate<Integer> p2 = m -> m > 5;

Predicate<Integer> between = p1.and(p2);
between.test(7);  // true: 7 > 5 && 7 < 10

Predicate<Integer> either = p1.or(p2);
either.test(7);  // true (both could be true; OR is still true)
```

### `Collection.removeIf(Predicate<? super E>)`

**`removeIf`** removes all elements matching the predicate—no manual iterator loop required.

```java
import java.util.ArrayList;
import java.util.List;

List<String> animals = new ArrayList<>(List.of("dog", "cat", "cow", "ant", "lion"));
animals.removeIf(animal -> animal.equals("ant"));
// "ant" removed; others unchanged
```

### Passing a `Predicate` into your own method (even/odd example)

```java
import java.util.Scanner;
import java.util.function.Predicate;

public class EvenOdd {

    public static boolean isEven(int number, Predicate<Integer> p) {
        return p.test(number);
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Please enter a number: ");
            int entered = scanner.nextInt();

            if (isEven(entered, n -> n % 2 == 0)) {
                System.out.println(entered + " is an even number");
            } else {
                System.out.println(entered + " is an odd number");
            }
        }
    }
}
```

You can assign the lambda to a **`Predicate<Integer>`** variable first, or inline it as shown—the types must match **`test(Integer)`** → **`boolean`**.

---

## Method references

### Idea (Java 8+)

A **method reference** is **syntactic sugar** for a lambda that **only** calls an existing method, with **no extra logic**. It often improves **readability** and reduces **boilerplate**.

**Syntax:** **`TargetReference::methodName`**

- **`::`** is the double colon (not `.`).

### When to use

- **Use** a method reference when the lambda is effectively “forward this call.”
- **Prefer a lambda** (or a separate method + reference) when you need **multiple steps**, conditions, or additional arguments beyond what the SAM supplies.

**Example:** printing each element:

```java
import java.util.List;

List<String> animals = List.of("dog", "cat", "cow", "lion");
animals.forEach(a -> System.out.println(a));   // lambda
animals.forEach(System.out::println);         // method reference — same idea
```

**`forEach`** on `Iterable` takes a **`Consumer<T>`** (`void accept(T t)`). **`println(String)`** matches **`Consumer<String>`** when the element type is `String`.

### Four forms (exam pattern)

#### 1. Reference to a static method

```java
import java.util.function.Function;

Function<String, Integer> f = Integer::parseInt;
int n = f.apply("123");  // 123
```

Lambda equivalent: `s -> Integer.parseInt(s)`.

#### 2. Reference to an instance method of a particular object (bound receiver)

```java
import java.util.function.Supplier;

String str = "hello";
Supplier<String> sup = str::toUpperCase;
System.out.println(sup.get());  // HELLO
```

Lambda equivalent: `() -> str.toUpperCase()`.

#### 3. Reference to an instance method of an arbitrary object of a given type (unbound: class as receiver)

```java
import java.util.function.Function;

Function<String, String> upper = String::toUpperCase;
System.out.println(upper.apply("hello"));  // HELLO
```

Lambda equivalent: `s -> s.toUpperCase()`.

#### 4. Reference to a constructor

```java
import java.util.ArrayList;
import java.util.function.Supplier;

Supplier<ArrayList<String>> maker = ArrayList::new;
ArrayList<String> list = maker.get();
```

Lambda equivalent: `() -> new ArrayList<>()`.

### Compatibility rules (critical)

1. The **referenced method** must be **applicable** to the **abstract method** of the **target functional interface**: **parameter types, count, and return type** must line up (including boxing and generic bounds where the compiler allows).
2. Method references **only** apply where a **functional interface** (SAM) is expected.

### When a method reference does *not* fit

If each element needs a **guard** or extra work, a bare **`System.out::println`** reference is wrong because **`Consumer`** only receives the element—you cannot inject the `if` into the reference without wrapping:

```java
// Needs a lambda (or a separate method referenced after extraction)
animals.forEach(animal -> {
    if (animal.startsWith("c")) {
        System.out.println(animal);
    }
});
```

You *could* extract **`void printIfStartsWithC(String animal)`** and use **`this::printIfStartsWithC`** (or a static helper) if the signature still matches **`Consumer<String>`**.

### Course tie-in: matching signatures for `Animals`

If a **static** or **instance** method **`display(String, int)`** has the **same parameter types and return type** as **`Animals.show`**, you can assign:

```java
Animals a = MainTest::display;  // if display is compatible
```

IDEs often suggest converting eligible lambdas to method references.

### Other functional types mentioned

| Interface   | Abstract method | Typical use                                      |
|------------|-----------------|--------------------------------------------------|
| `Consumer<T>` | `void accept(T t)` | Side effect on one value (e.g. `forEach`)   |
| `Function<T,R>` | `R apply(T t)` | Map input to output                          |
| `Supplier<T>`   | `T get()`    | Provide a value with no input (e.g. factory)     |
| `Predicate<T>` | `boolean test(T t)` | Boolean test                              |

---

## Switch expressions and enhanced `switch`

### Traditional `switch` (statement)

- **`break`** ends a branch; without **`break`**, execution **falls through** to the next **`case`**—a common source of bugs.
- Historically, `switch` was mainly a **control-flow statement**, not an expression—so you often **repeated** assignments like `dayName = ...` in every branch.

### Modern `switch` (expressions) — course highlights

- **Preview / evolution:** enhancements begin around **Java 12**, stabilized for **switch expressions** by **Java 14** (per course). **Java 21** adds further improvements (e.g. **`switch` pattern matching**).
- **`switch` as an expression** produces a **value** you assign to a variable.

**Arrow labels (`->`)** (no fall-through for that case arm as in the simple form shown in the course):

```java
int day = 3;
String dayName = switch (day) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    case 3 -> "Wednesday";
    default -> "Other";
};  // semicolon terminates the whole switch-expression statement
```

- **`break`** is **not** used to exit each arm in this style the way it is in classic fall-through `switch`.
- A **`switch` expression** must be **complete** (every path yields a value) and is typically terminated with **`;`** after the closing `}`.

### `yield`

Use **`yield`** when a **`case`** needs **multiple statements** or a **block**, and the **`switch` expression** must still **return one value** from that arm:

```java
int day = 3;
String message = switch (day) {
    case 1, 2, 3, 4, 5 -> {
        System.out.println("weekday branch");
        yield "workday";
    }
    case 6, 7 -> "weekend";
    default -> "invalid day";
};
```

### Rules and pitfalls (exam-focused)

- **Do not mix** **`:` case labels** and **`->`** arms **in the same** `switch`—**compilation error**.
- **`yield`** is for **expression** `switch` **returning values** from a block arm; do not confuse with old `break value` preview-era phrasing—know **`yield`** for modern materials.
- **`break`** in **arrow** `switch` is **restricted** / **unnecessary** in the simple arms; the course demonstrates that **`break`** does not pair cleanly with **`yield`** in the same scoped case the way beginners might try.

### Pattern matching for `switch` (Java 21 — type patterns)

Instead of a long **`instanceof`** chain, you can **dispatch on runtime type** with **`switch`**:

```java
Object obj = 42;

String desc = switch (obj) {
    case Integer i -> "Integer: " + i;
    case String s  -> "String: " + s;
    default        -> "unknown type";
};
```

**Exam note:** In **`case` type patterns**, you typically need a **binding variable** (e.g. **`Integer i`**) where the language requires it—differing from older `instanceof`-only style mentally, but aligned with pattern variable rules in `switch`.

### `enum` and exhaustiveness

For **`switch` expressions** over an **`enum`**, the compiler checks **coverage** of **all constants** (depending on cases + **`default`**).

- If **at least one constant** is not handled and there is **no `default`**, you can get: **`switch expression does not cover all possible input values`**.
- Adding a **`default`** **can** resolve the error if you intentionally do not list every enum constant individually.

### Traditional fall-through demo (why `break` mattered)

Without **`break`**, after a matching **`case`**, execution continues into subsequent **`case`** bodies until a **`break`**—so multiple cases run. **`switch` expressions with `->`** avoid that pattern for simple arms.

---

## Key takeaways

- **Functional interface** = **one** abstract method; **`default`/`static`** methods allowed; **`@FunctionalInterface`** documents and enforces.
- **Marker interface** = **no** members; used for **tagging** (`Serializable`, `Cloneable`, …).
- **Lambda** = compact SAM implementation: **params `->` body**; parameter **names** are local; **types** must match the abstract method.
- **`Predicate<T>`**: **`test`**, compose with **`and` / `or` / `negate`**; **`removeIf`** on collections.
- **Method reference** = **`Type::method`** or **`instance::method`**; only when delegation matches the **SAM signature**; **`forEach(System.out::println)`** is idiomatic.
- **`switch` expression**: value-producing **`switch`**, **`->`** arms, **`yield`** in blocks, **semicolon** after `}`; **pattern matching** and **`enum`** exhaustiveness are **high-yield** exam topics in Java 21 tracks.

---

## Common pitfalls

1. Thinking **`@FunctionalInterface`** is required for lambdas to work—it is **not**; the SAM rule is.
2. **Marker vs functional:** an empty interface is **not** a functional interface for lambda assignment.
3. **`Predicate` typo logic:** using **`equals`** on **`String`** is **case-sensitive**; **`equalsIgnoreCase`** differs.
4. **Method reference** on **`println`** only works when the **SAM** argument lines up (e.g. **`Consumer<String>`** vs raw **`println(Object)`** overload resolution—usually fine with **`String`** list).
5. **`switch` expression**: forgetting the **final `;`**, mixing **`:`** and **`->`**, or missing **`default`/`cases`** so the **`enum`/sealed** coverage fails.
6. **Fall-through** in **legacy** `switch`: removing all **`break`** statements causes **multiple cases** to run.

---

## Likely exam questions (with answers)

**Q1. What makes an interface a functional interface?**  
**A.** It has **exactly one abstract method** (SAM). `default`/`static` methods do not count toward that limit.

**Q2. What does `@FunctionalInterface` do?**  
**A.** It is a **compile-time** annotation that marks intent and **causes an error** if the interface is no longer a valid functional interface (e.g. **two** abstract methods).

**Q3. Can a lambda’s parameter names differ from the abstract method’s names?**  
**A.** **Yes.** Names are arbitrary; **types and arity** must match the abstract method.

**Q4. What is the single abstract method of `Predicate<T>`?**  
**A.** **`boolean test(T t)`**.

**Q5. How do you combine two predicates so both must be true?**  
**A.** **`p1.and(p2)`** (then call **`test`**). For OR, **`p1.or(p2)`**; for negation, **`p.negate()`**.

**Q6. Which collection method removes elements matching a condition using a `Predicate`?**  
**A.** **`removeIf(Predicate<? super E> filter)`**.

**Q7. What is the syntax for a method reference to a static method?**  
**A.** **`ContainingType::methodName`**, e.g. **`Integer::parseInt`**.

**Q8. When is `str::toUpperCase` valid as a `Supplier<String>`?**  
**A.** When **`str`** is a **`String` instance** in scope: **`Supplier`** takes **no args** and **`get()`** invokes **`toUpperCase()`** on that fixed receiver.

**Q9. What does `String::toUpperCase` mean as `Function<String, String>`?**  
**A.** **Unbound** instance reference: the **`apply`** argument is the receiver **`s -> s.toUpperCase()`**.

**Q10. What is a `switch` expression, and how does `->` differ from classic fall-through cases?**  
**A.** A **`switch` that yields a value**. With **`->`**, the matching arm is selected and **does not fall through** to the next case like unbroken **`:`** legacy chains.

**Q11. When do you use `yield`?**  
**A.** In a **`switch` expression**, inside a **`case`** that uses a **block** `{ ... }` to run multiple statements and then **produce the case’s value**.

**Q12. Why might `switch` on an `enum` fail to compile without `default`?**  
**A.** **`switch` expressions** require **exhaustive** handling of inputs; for **`enum`**, **all constants** must be covered by **`case`** labels or a **`default`** (compiler error if not).

**Q13. What Java version feature lets you replace some `instanceof` chains with `switch` on `Object`?**  
**A.** **Pattern matching for `switch`** (presented in the course as a **Java 21** enhancement).

---

## Appendix: Calculator lab (optional video 7)

The **“Simple Calculator app with Lambda”** lesson reinforces the same ideas: define a **functional interface** for an operation, pass it into a method, and supply a **lambda** instead of an **anonymous class**.

**`Operation` SAM** — `void performOperation(double x, double y)` (course naming).

**`Calculator.calculate(double x, double y, Operation op)`** — delegates to **`op.performOperation(x, y)`**.

**Call site** — replace verbose `new Operation() { ... }` with lambdas for sum, difference, product, and quotient (production code should guard division by zero):

```java
@FunctionalInterface
public interface Operation {
    void performOperation(double x, double y);
}

public class Calculator {
    public void calculate(double x, double y, Operation operation) {
        operation.performOperation(x, y);
    }
}

// Example usage (after reading two doubles a and b from the user):
Calculator calculator = new Calculator();
calculator.calculate(a, b, (x, y) -> System.out.println("Sum: " + (x + y)));
calculator.calculate(a, b, (x, y) -> System.out.println("Diff: " + (x - y)));
calculator.calculate(a, b, (x, y) -> System.out.println("Product: " + (x * y)));
calculator.calculate(a, b, (x, y) -> System.out.println("Quotient: " + (x / y)));
```

**Exam angle:** this is the **strategy pattern** with a **functional interface**: behavior (**which operation**) is **injected** as the third argument; lambda parameter names **`(num1, num2)`** vs **`(x, y)`** are arbitrary as long as positions match **`performOperation`**.

---

## Sources

Course subtitles merged from this module:

1. Section Overview  
2. Marker and Functional Interfaces  
3. Lambda Expression  
4. Predicate  
5. Method Reference  
6. Switch Expression (Enhanced Switch Statement)  
7. Simple Calculator app with Lambda (appendix)
