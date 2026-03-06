# Module 05 -- Array

### Q: What are the two valid syntaxes for declaring an array in Java?
`type[] name` (e.g. `int[] arr`) or `type name[]` (e.g. `int arr[]`). The first is preferred in Java style.

### Q: How do you instantiate an array and what are the default values?
Use `new type[length]`, e.g. `int[] a = new int[5];`. Numeric elements default to 0, boolean to false, reference types to null.

### Q: How do you declare and initialize an array with a literal?
Use curly braces: `int[] arr = { 10, 20, 30 };` or `String[] s = { "a", "b" };`. The size is inferred; you cannot specify length in the literal.

### Q: What is array.length and is it a method?
`array.length` is a final field (not a method), so you use it without parentheses. It gives the number of elements.

### Q: When does ArrayIndexOutOfBoundsException occur?
When you use an index that is negative or greater than or equal to the array length.

### Q: How do you sort an array and how does Arrays.sort() order String arrays?
Use `Arrays.sort(array)`. For primitives it sorts numerically; for objects (including String) it uses natural order—for String, lexicographic order.

### Q: How does Arrays.binarySearch() work and what does a negative return value mean?
The array must be sorted. Returns the index of the key if found. If not found, returns `-(insertion point) - 1`, so you can detect "not found" and compute where the key would be inserted.

### Q: How do you create a 2D array and what is a jagged array?
Declare with two dimensions: `int[][] matrix = new int[3][4];` or with literals: `int[][] m = { {1,2}, {3,4} };`. A jagged array has rows of different lengths (e.g. `int[][] j = { {1,2}, {3,4,5} };`).

### Q: In `int[] a, b;` versus `int a[], b;`, what type is each variable?
In `int[] a, b;` both a and b are int arrays. In `int a[], b;` only a is an array; b is an int. Exam questions often test this.
