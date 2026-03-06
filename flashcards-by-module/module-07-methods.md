# Module 07 -- Methods

### Q: What are the five components of a method declaration in Java?
Access modifier (e.g. public, private), optional specifier (static, final, abstract), return type (required—a type or void), method name, and parameter list in parentheses.

### Q: What happens if a non-void method is missing a return statement?
The code will not compile. Every code path in a non-void method must return a value whose type matches (or is assignable to) the declared return type.

### Q: What is the syntax for declaring a var-args parameter and what are the rules?
Use three dots after the type: `int... nums`. Inside the method, nums is treated as an int[] array. Rules: at most one var-args parameter per method, and it must be the last parameter.

### Q: Can you call a var-args method with zero arguments?
Yes. `void greet(String... names)` can be called as `greet()`; names will be an empty array of length 0.

### Q: What is method overloading?
Defining multiple methods with the same name but different parameter lists (different number, type, or order of parameters) in the same class.

### Q: Does changing only the return type create a valid overload?
No. Two methods with the same name and same parameter list but different return types cause a compile error. The parameter list must differ.

### Q: What is the method resolution order when overloads exist?
The compiler chooses: 1) exact type match, 2) widening (e.g. int to long), 3) autoboxing (e.g. int to Integer), 4) var-args. It never narrows automatically.

### Q: In Java, is method argument passing by value or by reference?
Always by value. For primitives, a copy of the value is passed. For objects, a copy of the reference is passed—the caller's reference cannot be changed, but the object it points to can be mutated.

### Q: If a method accepts int[] and modifies arr[0] = 99, does the caller see the change?
Yes. The array reference is copied, but both references point to the same array object on the heap, so changes to elements are visible to the caller.
