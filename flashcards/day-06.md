# Day 6 -- Operators (Part 2)

### Q: How does the conditional AND operator `&&` behave (short-circuit)?
`&&` evaluates left to right. The result is `true` only if both operands are true. If the first operand is **false**, the second operand is **not evaluated** (short-circuit); the result is false without checking the second condition.

### Q: How does the conditional OR operator `||` behave (short-circuit)?
`||` evaluates left to right. The result is `true` if at least one operand is true. If the first operand is **true**, the second operand is **not evaluated** (short-circuit); the result is true without checking the second condition.

### Q: When is the second operand of `&&` evaluated? When is the second operand of `||` evaluated?
For `&&`, the second operand is evaluated only if the first is **true**. For `||`, the second operand is evaluated only if the first is **false**.

### Q: What is the syntax and meaning of the ternary operator?
Syntax: `condition ? valueIfTrue : valueIfFalse`. The condition (boolean expression) is evaluated; if true, the expression evaluates to the value after `?`, otherwise to the value after `:`. Example: `result = (number1 < number2) ? true : false;`

### Q: What does the bitwise AND operator `&` do on two integers?
It compares corresponding bits of both operands. If both bits are 1, the result bit is 1; otherwise it is 0. Example: `8 & 9` (binary 1000 & 1001) gives 1000, i.e., 8.

### Q: What does the bitwise OR operator `|` do on two integers?
It compares corresponding bits. If either bit is 1, the result bit is 1; only when both are 0 is the result 0. Example: `8 | 9` (1000 | 1001) gives 1001, i.e., 9.

### Q: What does the bitwise exclusive OR operator `^` do?
It compares corresponding bits. If the two bits are **different**, the result bit is 1; if they are the same, the result bit is 0. Example: `8 ^ 9` (1000 ^ 1001) gives 0001, i.e., 1.

### Q: What does the bitwise complement operator `~` do?
It is a unary operator that inverts every bit: 0 becomes 1 and 1 becomes 0. The value is treated as a 32-bit (int) pattern, so the result is often negative (two's complement). Example: `~8` gives -9, not 7.

### Q: What does the signed left shift operator `<<` do?
It shifts the bit pattern of the left operand left by the number of positions given by the right operand, filling low-order bits with zeros. Example: `8 << 2` shifts 1000 left by 2, yielding 100000 (32 in decimal).

### Q: What does the signed right shift operator `>>` do?
It shifts the bit pattern of the left operand right by the number of positions given by the right operand, dropping the low-order bits. Example: `8 >> 2` yields 10 in binary, i.e., 2 in decimal.

### Q: What is the range of values for the char data type and how is it represented?
`char` is an unsigned 16-bit integer type representing Unicode code units. Its range is **0 to 65,535**. It can be used in integer arithmetic and has a numeric value (e.g., ASCII/Unicode code point).

### Q: How can you assign a numeric value to a char variable?
You can assign either a character literal in single quotes (e.g., `char c = 'H';`) or the corresponding integer (e.g., `char c = 72;`). The compiler interprets the integer as the character with that code point (e.g., 72 is 'H' in ASCII).

### Q: Why do you need an explicit cast when assigning an int to a char?
Because `int` is 32-bit and can hold values outside the char range (0–65535). Java does not allow implicit narrowing, so you must cast: `char letterTwo = (char) numOne;`.

### Q: In char arithmetic, what is the type of `letterOne + 3` if `letterOne` is char?
The result is **int**. Binary numeric promotion promotes `char` to `int` in arithmetic, so `letterOne + 3` is an int (e.g., 70). To store it in a char you must cast: `char letterTwo = (char)(letterOne + 3);`.

### Q: How does operator precedence affect the evaluation of `5 + 2 * 4`?
Multiplication has higher precedence than addition, so `2 * 4` is evaluated first (8), then `5 + 8` gives **13**, not 28. Use parentheses to change order: `(5 + 2) * 4` is 28.

### Q: How do parentheses affect operator precedence?
Any expression enclosed in parentheses is evaluated **first**, before applying the normal precedence rules. Parentheses override the default order of evaluation.

### Q: In an expression with division, modulus, multiplication, and addition (no parentheses), which operations are performed first?
Division, modulus, and multiplication (multiplicative operators) have higher precedence than addition (additive). Among operators of the same precedence, evaluation is left to right. So multiplicative operations are done first, then additive.

### Q: What is a Java expression and what does it evaluate to?
An expression is a combination of variables, operators, and method calls that evaluates to a **single value**. Examples: `5 + 8`, `number1 == number2`, `maxSpeed = 280`. Expressions do not stand alone as units of execution; they are used inside statements.

### Q: What is a Java statement and how do you recognize it?
A statement is a complete unit of execution. A statement typically **ends with a semicolon** (`;`). Expressions are often part of statements (e.g., `int result = 5 + 8;` is a statement containing an expression).

### Q: What is a block in Java and how is it denoted?
A block is a group of zero or more statements enclosed in **curly braces** `{ }`. Blocks define scope and can contain multiple statements. Control-flow constructs (e.g., if, for, methods) use blocks to group code.
