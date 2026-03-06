# Module 06 -- Control Flow Statements

### Q: When are curly braces optional in an if or else block?
Only when the block contains exactly one statement. Without braces, a second line is not part of the if and always runs—a common exam trap.

### Q: Which types are allowed as the switch expression in Java?
byte, short, int, char (and their wrappers), String, and enum types. Not long, float, double, or boolean.

### Q: What is fall-through in a switch and when does it happen?
Without a break, execution falls through to the next case(s) until a break or the end of the switch. So if case 3 has no break, the code for case 3, 4, 5, and default can all run.

### Q: What is the difference between return and break in a switch?
break exits only the switch; execution continues after the switch. return exits the current method entirely.

### Q: What are the three parts of a for loop and in what order do they run?
Initialization (once), condition (each iteration; must be boolean), update (after each iteration). Order: init → condition → body (if true) → update → condition again.

### Q: What is the enhanced for loop (for-each) and what is its main limitation?
Syntax: `for (Type item : arrayOrCollection) { }`. It iterates over each element; you cannot access the current index. Use a regular for loop when you need the index.

### Q: What is the key difference between do-while and while?
do-while checks the condition after the body, so the body runs at least once. while checks before each iteration, so the body may never run.

### Q: What does break do in a loop? What does continue do?
break terminates the loop immediately; control moves to the next statement after the loop. continue skips the rest of the current iteration and goes to the loop condition (and next iteration); in a for loop the update still runs.

### Q: Can you use break or continue outside a loop?
break can be used in a loop or switch. continue can be used only inside a loop. Using either in an if without a loop (or continue in a switch) causes a compile error.

### Q: What is a labeled loop and how do you use break/continue with a label?
A label is a name followed by a colon before the loop (e.g. `outer: for (...) { }`). `break outer;` exits the labeled loop. `continue outer;` jumps to the next iteration of the labeled loop. Used in nested loops to control which loop is affected.
