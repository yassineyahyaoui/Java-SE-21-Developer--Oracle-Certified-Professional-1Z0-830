# Day 8 -- Control Flow (Part 1)

### Q: What are the four main types of if statements in Java?
if, if-else, if-else-if ladder, and nested if. The if-else-if ladder executes one condition from multiple; nested if means an if block inside another if block (inner executes only when outer is true).

### Q: When are curly braces optional in an if or else block?
Only when the block contains exactly one statement. You can write `if (x > 0) System.out.println("yes");` without braces. Any additional line is not part of the if and always runs—a common trap.

### Q: What is the "single-line if" trap regarding multiple statements?
Without braces, only the first statement after the if is conditional. A second line is outside the if block and always executes. Use braces when you have more than one statement.

### Q: What is the ternary operator and how is it used?
The conditional operator `?:` — condition ? valueIfTrue : valueIfFalse. It is shorthand for a simple if-else that assigns or returns a value (e.g. `result = score > 50 ? "pass" : "fail"`).

### Q: Which types are allowed as the switch expression in Java?
byte, short, int, char (and their wrappers), long, String, and enum types. The expression is in parentheses after the switch keyword.

### Q: What must case values be in a switch statement?
Literals or constants of the same type as the switch expression. Variables are not allowed. Case values must be unique or you get a compile-time error.

### Q: What is fall-through in a switch and when does it happen?
Without a break, execution falls through to the next case(s) until a break or the end of the switch. So if case 3 has no break, case 3, 4, 5, etc. (and default) can all run.

### Q: How do you make multiple cases execute the same code in a switch?
Group cases by listing them with colons and no code between: `case 1: case 2: case 3: day = "weekday"; break;` Only the last case in the group needs the shared code and break.

### Q: What is the difference between return and break in a switch?
break exits only the switch; execution continues after the switch. return exits the current method, so nothing after the switch in that method runs. Use return in default when you want to stop the method (e.g. invalid input).

### Q: In an if-else-if ladder, what happens once a condition is true?
Only that block runs; the rest of the conditions are not evaluated. If you use separate if statements (no else if), each condition is checked and multiple blocks can execute.

### Q: In a nested if, when does the inner if run?
Only when the outer if condition is true. The inner condition is evaluated only inside the outer if block.

### Q: Can you use the logical complement operator in an if condition for a boolean?
Yes. `if (!control)` is the same as `if (control == false)` or `if (control != true)`. For a boolean variable, `if (control)` is equivalent to `if (control == true)`.

### Q: What does the default case in a switch do?
It runs when no case value matches the switch expression. It is optional. Typically used to handle invalid or unexpected values.

### Q: Is break required in every case of a switch?
No. Break is optional. Without it, execution falls through to the next case. It is recommended to use break (or return) when you do not want fall-through.
