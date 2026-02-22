# Day 7 -- Arrays + Wrapper Classes

### Q: What are the two valid syntaxes for declaring an array in Java?
You can use `type[] name` (e.g. `int[] arr`) or `type name[]` (e.g. `int arr[]`). Both declare an array; the first is preferred in Java style.

### Q: How do you instantiate an array and what are the default values for elements?
Use `new type[length]`, e.g. `int[] a = new int[5];`. Numeric elements default to 0, boolean to false, and reference types to null.

### Q: How do you declare and initialize an array with a literal in one step?
Use curly braces: `int[] arr = { 10, 20, 30 };` or `String[] s = { "a", "b" };`. The size is inferred; you cannot specify length in the literal.

### Q: How do you access array elements and what is the index range?
Elements are accessed by zero-based index: `arr[0]` is the first element, `arr[arr.length - 1]` is the last. Valid indices are 0 through length - 1.

### Q: What is array.length and is it a method?
`array.length` is a final field (not a method), so you use it without parentheses. It gives the number of elements in the array.

### Q: When does ArrayIndexOutOfBoundsException occur?
It is thrown when you use an index that is negative or greater than or equal to the array length (e.g. accessing `arr[5]` on an array of length 5).

### Q: How do you sort an array with Arrays.sort() and how does it order String arrays?
Use `Arrays.sort(array)`. For primitives it sorts numerically; for objects (including String) it uses natural order—for String, lexicographic (dictionary) order.

### Q: How does Arrays.binarySearch() work and what does a negative return value mean?
The array must be sorted. The method returns the index of the key if found. If not found, it returns `-(insertion point) - 1`, where insertion point is where the key would be inserted to keep order.

### Q: How do you create and initialize a 2D array in Java?
Declare with two dimensions: `int[][] matrix = new int[3][4];` or with literals: `int[][] m = { {1,2}, {3,4} };`. Rows can have different lengths (jagged).

### Q: What is a jagged array?
A jagged array is a 2D (or higher) array where each row can have a different length, e.g. `int[][] jagged = { {1,2}, {3,4,5} };`. Only the first dimension size is required when using `new`.

### Q: Why do wrapper classes (Integer, Double, etc.) exist in Java?
Collections and generic types (e.g. `List<T>`) work only with objects, not primitives. Wrapper classes let you store and pass primitive values as objects.

### Q: How do you convert between primitive and wrapper using valueOf and xxxValue()?
Use `Integer.valueOf(5)` or `Integer.valueOf("42")` to get an Integer. Use `intValue()`, `doubleValue()`, etc. on the wrapper to get the primitive: `integerObj.intValue()`.

### Q: What is autoboxing?
Autoboxing is the automatic conversion of a primitive value to its corresponding wrapper object when needed (e.g. assigning an `int` to an `Integer` or passing it to a method that expects `Integer`).

### Q: What is unboxing?
Unboxing is the automatic conversion of a wrapper object to its primitive value when needed (e.g. assigning an `Integer` to an `int` or using it in arithmetic).

### Q: When does NullPointerException occur with wrapper types?
When you unbox a null wrapper reference—e.g. `Integer n = null; int x = n;` or `n + 1`—the JVM tries to unbox null and throws NullPointerException.

### Q: What does Arrays.binarySearch() return if the key is not found?
It returns `-(insertion point) - 1`. For example, if the key would be inserted at index 2, the return value is -3. This lets you both detect “not found” and compute the insertion point.

### Q: Can you use both type[] name and type name[] in the same declaration for multiple variables?
Yes. In `int[] a, b;` both a and b are int arrays. In `int a[], b;` only a is an array; b is an int. Exam questions often test this distinction.

### Q: How do you create a 3D array and access an element?
Declare and create with three dimensions: `int[][][] cube = new int[2][3][4];`. Access with three indices: `cube[i][j][k]`. Dimensions can be jagged by creating each level separately.
