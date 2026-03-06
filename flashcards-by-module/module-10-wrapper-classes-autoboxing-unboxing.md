# Module 10 -- Wrapper Classes, Auto-Boxing and Unboxing

### Q: Why do wrapper classes (Integer, Double, etc.) exist in Java?
Collections and generic types (e.g. List<T>) work only with objects, not primitives. Wrapper classes let you store and pass primitive values as objects.

### Q: How do you convert between primitive and wrapper using valueOf and xxxValue()?
Use `Integer.valueOf(5)` or `Integer.valueOf("42")` to get an Integer. Use `intValue()`, `doubleValue()`, etc. on the wrapper to get the primitive: `integerObj.intValue()`.

### Q: What is autoboxing?
Automatic conversion of a primitive value to its corresponding wrapper object when needed (e.g. assigning an int to an Integer or passing it to a method that expects Integer).

### Q: What is unboxing?
Automatic conversion of a wrapper object to its primitive value when needed (e.g. assigning an Integer to an int or using it in arithmetic).

### Q: When does NullPointerException occur with wrapper types?
When you unbox a null wrapper reference—e.g. `Integer n = null; int x = n;` or `n + 1`—the JVM tries to unbox null and throws NullPointerException.

### Q: Why can Integer == return true for two boxed values without using equals()?
Only when the value is in the cache range -128 to 127. Within that range, boxing may reuse the same object; outside it, new Integer instances are created and == is false. Always use equals() for value comparison.
