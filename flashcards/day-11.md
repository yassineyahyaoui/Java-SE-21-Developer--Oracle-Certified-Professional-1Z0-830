# Day 11 -- Methods

### Q: What are the five components of a method declaration in Java?
Access modifier (e.g. `public`, `private`), optional specifier (`static`, `final`, `abstract`), return type (required -- a data type or `void`), method name, and parameter list inside parentheses.

### Q: When does a method execute its code?
A method only executes when it is called. It runs from the first statement to the last statement in the body, or until a `return` statement is reached.

### Q: What happens if a non-void method is missing a return statement?
The code will not compile. Every code path in a non-void method must return a value whose type matches (or is assignable to) the declared return type.

### Q: What is the difference between a standard library method and a user-defined method?
Standard library methods are built into the JDK (e.g. `Math.min()`, `Math.pow()`, `System.out.println()`). User-defined methods are written by the programmer to perform custom tasks.

### Q: What does `Math.pow(2, 10)` return and what is its type?
It returns `1024.0` as a `double`. To get an `int`, you must cast: `int result = (int) Math.pow(2, 10);`.

### Q: What is the syntax for declaring a var-args parameter?
Use three dots after the type: `int... nums`. Inside the method, `nums` is treated as an `int[]` array.

### Q: What are the two rules for var-args parameters?
1) A method can have at most one var-args parameter. 2) The var-args parameter must be the last parameter in the parameter list.

### Q: Is `static void test(int... a, int... b)` valid?
No. Only one var-args parameter is allowed per method, and it must be the last parameter.

### Q: Can you call a var-args method with zero arguments?
Yes. `void greet(String... names)` can be called as `greet()` (names will be an empty array of length 0).

### Q: What is method overloading?
Defining multiple methods with the same name but different parameter lists (different number, type, or order of parameters) in the same class.

### Q: Does changing only the return type create a valid overload?
No. Two methods with the same name and same parameter list but different return types cause a compile error. The parameter list must differ.

### Q: Given `void test(int a)` and `void test(long a)`, what does `test(5)` call?
It calls `test(int a)` because the compiler picks the most specific match. An `int` literal matches `int` exactly before widening to `long`.

### Q: What is the method resolution order when overloads exist?
The compiler chooses: 1) exact type match, 2) widening (e.g. `int` to `long`), 3) autoboxing (e.g. `int` to `Integer`), 4) var-args. It never narrows automatically.

### Q: In Java, is method argument passing "by value" or "by reference"?
Always by value. For primitives, a copy of the value is passed. For objects, a copy of the reference is passed -- the original reference cannot be changed, but the object it points to can be mutated.

### Q: What does the following print? `int a = 5; modify(a); System.out.println(a);` where `modify` sets its parameter to 100.
It prints `5`. Primitives are passed by value, so modifying the parameter inside the method does not affect the caller's variable.

### Q: If a method accepts `int[]` and modifies `arr[0] = 99`, does the caller see the change?
Yes. The array reference is copied, but both references point to the same array object on the heap, so changes to array elements are visible to the caller.
