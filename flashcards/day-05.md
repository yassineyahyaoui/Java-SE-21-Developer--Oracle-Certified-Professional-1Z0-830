# Day 5 -- Operators (Part 1)

### Q: What is an operator and what is an operand?
An operator is a special symbol that performs a specific operation (e.g., arithmetic, logical). An operand is the value that the operator acts on. In `5 + 4`, `+` is the operator and `5` and `4` are the operands.

### Q: What are the five arithmetic operators in Java and what does each do?
The five arithmetic operators are: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), and `%` (remainder/modulus). Division of two integers yields an integer; with at least one floating-point operand the result is a floating-point type.

### Q: How does the `+` operator behave differently with strings vs numbers?
With numbers, `+` performs numeric addition. With at least one String operand, `+` performs string concatenation (the other operand is converted to a String). Example: `"Java " + "programming"` yields `"Java programming"`.

### Q: What does the remainder operator `%` return?
The `%` operator divides the left operand by the right and returns the remainder. For example, `35 % 20` is `15`; `8.4 % 4.2` can be `0.0` when the division is exact (subject to floating-point precision).

### Q: What is the result type of an arithmetic expression like `8.4 / 4.2`?
The result type is determined by the operands. If both operands are numeric and at least one is a floating-point type (e.g., `double`), the result is that floating-point type (e.g., `double`). Integer division yields `int`.

### Q: What do the compound assignment operators `+=`, `-=`, `*=`, `/=`, and `%=` do?
Each performs the corresponding operation with the left and right operands and assigns the result to the left operand. For example, `z += x` is equivalent to `z = z + x`; same idea for `-=`, `*=`, `/=`, and `%=`.

### Q: If `z` is 35 and `x` is 20, what is the value of `z` after `z -= x`?
`z` becomes `15`, because `z -= x` is equivalent to `z = z - x`, i.e., `z = 35 - 20`.

### Q: What are the unary operators in Java and what does each do?
Unary plus `+` (positive value, rarely used); unary minus `-` (negates the value); `++` (increment by 1); `--` (decrement by 1); `!` (logical complement, inverts a boolean).

### Q: What is the difference between prefix and postfix for `++` and `--`?
With prefix (`++x` or `--x`), the value is incremented or decremented first, then the new value is used in the expression. With postfix (`x++` or `x--`), the current value is used in the expression first, then the variable is incremented or decremented.

### Q: If `result` is 4.7, what is printed by `System.out.println(result++);` and what is `result` after?
`4.7` is printed (postfix: use value then increment). After the statement, `result` is `5.7`.

### Q: If `result` is 5.7, what is printed by `System.out.println(++result);` and what is `result` after?
`6.7` is printed (prefix: increment first then use value). After the statement, `result` is `6.7`.

### Q: What does the logical complement operator `!` do?
It inverts a boolean: `!true` is `false` and `!false` is `true`. It is a unary operator and applies only to boolean operands.

### Q: What are the equality operators and what type do they return?
`==` checks if two operands are equal; `!=` checks if they are not equal. Both return a **boolean** result (`true` or `false`).

### Q: What are the relational operators and what type do they return?
Relational operators are `>`, `<`, `>=`, and `<=`. They compare the left operand to the right and return a **boolean** (`true` or `false`).

### Q: If `a` is 2 and `b` is 5, what are the values of `a == b`, `a != b`, `a < b`, and `a <= b`?
`a == b` is `false`; `a != b` is `true`; `a < b` is `true`; `a <= b` is `true`. All results are boolean.

### Q: Why might floating-point arithmetic show "loss of precision" in output (e.g., 12.600000000000001)?
Computers represent decimal numbers in binary; some decimal values cannot be represented exactly, so small rounding errors occur. This is inherent to floating-point representation, not a bug in the expression itself.
