# Day 9 -- Control Flow (Part 2)

### Q: What are the three parts of a for loop and in what order do they run?
Initialization (runs once), condition (evaluated each iteration; must be boolean), and update (runs after each iteration). Order: init → condition → body (if true) → update → condition again.

### Q: Can you declare multiple variables in the for loop initialization?
Yes, if they are the same type: `for (int a = 0, b = 1; a <= 5 && b < 11; a++, b++)`. You cannot mix types (e.g. int and long) in the same init—compile error.

### Q: What is the scope of a variable declared in the for loop header?
It is only visible inside the for loop. Using that variable after the loop (e.g. printing "last value of i") causes a compile error unless the variable was declared before the for.

### Q: Can the update part of a for loop be in the loop body instead of the header?
Yes. You can write `for (int i = 1; i <= 10;) { ... i++; }`. The update is optional in the parentheses.

### Q: How do you write an infinite loop with for?
Use empty condition (two semicolons): `for (;;) { ... }`. The loop runs until something inside (e.g. break or return) exits it.

### Q: In a nested for loop, how many times does the inner body run in total?
Inner iterations × outer iterations. Example: outer 3 times, inner 6 times → inner body runs 3 × 6 = 18 times.

### Q: What is the enhanced for loop (for-each) and what is its syntax?
It iterates over an array or Iterable. Syntax: `for (Type item : arrayOrCollection) { ... }`. Each element is assigned to `item` in order; no index variable.

### Q: What is the main limitation of the for-each loop?
You cannot access the current index. Use a regular for loop when you need the index (e.g. `for (int i = 0; i < arr.length; i++)`).

### Q: How do you iterate over the characters of a String with for-each?
Use `toCharArray()`: `for (char ch : str.toCharArray()) { ... }`. This converts the String to a char array so for-each can iterate over each character.

### Q: When is the condition checked in a while loop?
Before each iteration. If the condition is false at the start, the body never runs. The loop body usually updates a variable so the condition eventually becomes false.

### Q: How do you implement factorial with a while loop?
Use a loop that multiplies a result by the current number and then decrements the number: `while (n > 0) { result *= n; n--; }`. Handle n < 0 (undefined) and n == 0 or 1 (result 1) separately.

### Q: How do you create an infinite loop with while?
Use a condition that is always true: `while (true) { ... }`. Exit with break or return inside the loop.

### Q: If you write code after a while(true) loop with no break inside, what happens?
You get an unreachable code compile error. The compiler knows the loop never ends, so code after it is unreachable.

### Q: Why might code after while(true) not give an unreachable-code error?
If the condition is a variable (e.g. `while (isRunning)`), the compiler assumes it might change and does not report unreachable code. If you use `final boolean b = true; while (b)` then code after is unreachable again.

### Q: What is the key difference between do-while and while?
In do-while the body runs at least once; the condition is checked after the body. In while the condition is checked first, so the body might never run.

### Q: In do-while, when is the condition evaluated?
After each execution of the loop body. If true, the loop continues; if false, the loop ends and execution goes to the statement after the do-while.
