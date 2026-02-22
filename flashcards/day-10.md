# Day 10 -- Control Flow (Part 3) + Switch Expressions

### Q: What does the break keyword do in a loop or switch?
It terminates the loop or switch immediately. Control moves to the next statement after the loop or switch. In a for loop, the update expression is not run when break executes.

### Q: What does the continue keyword do in a loop?
It skips the rest of the current iteration and goes to the loop condition (and then next iteration). The update part of a for loop still runs before the condition is rechecked.

### Q: Can you use break in an if statement without a loop or switch?
No. Using break outside a loop or switch causes a compile error: "break cannot be used outside of a loop or switch."

### Q: Can you use continue in an if or switch?
No. continue is only valid inside a loop. Using it in an if (without a loop) or in a switch causes a compile error.

### Q: What does return do when used in a method?
It exits the current method and returns control to the caller. Any code after the return in that method is unreachable. In void methods you use `return;` with no value.

### Q: If the first statement in a method is return, what happens to the rest of the method?
The compiler reports an unreachable code error for every statement after that return. The method always exits at return, so later code can never run.

### Q: What is a labeled loop and how do you define it?
A loop with a name so you can target break or continue. Write a label (valid identifier) followed by a colon before the loop: `outer: for (...) { ... }`.

### Q: How do you use break with a label in nested loops?
Write `break labelName;` (e.g. `break outer;`). Execution exits the labeled loop, not just the innermost one. Without the label, break only exits the innermost loop.

### Q: How do you use continue with a label?
Write `continue labelName;`. Execution jumps to the next iteration of the labeled loop, skipping the rest of the inner loop body and any inner loops for that iteration.

### Q: In a while loop with continue, why must the update (e.g. index++) be placed carefully?
If continue runs before the update, the loop variable never changes and you can get an infinite loop. Place the update so it runs even when continue is used, or use a for loop where the update is in the header.

### Q: What is the Fibonacci sequence and how is the next number computed?
Each number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, ... So next = fibPrevious + fibCurrent; then shift: fibPrevious = fibCurrent, fibCurrent = next.

### Q: How do you implement the Fibonacci series with a for loop?
Use two variables (e.g. fibPrev, fib) and a loop: print fibPrev; sum = fibPrev + fib; fibPrev = fib; fib = sum; repeat. Loop counter controls how many numbers to print.

### Q: Why might the compiler not report unreachable code after while(true)?
If the loop contains a break (or return), the compiler considers that the loop may exit, so code after the loop is reachable. Without any exit path, code after while(true) is unreachable.

### Q: When you use return in a switch case instead of break, what is the effect?
The entire method exits at that point. Nothing after the switch runs. Useful in default for invalid input when you want to stop the method and avoid further output.
