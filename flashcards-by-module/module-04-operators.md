# Module 04 -- Operators

### Q: What are the five arithmetic operators in Java?
`+`, `-`, `*`, `/`, and `%` (remainder). Division of two integers yields an integer; with at least one floating-point operand the result is floating-point.

### Q: How does the `+` operator behave with strings vs numbers?
With numbers, `+` performs addition. With at least one String operand, `+` performs string concatenation (the other operand is converted to String).

### Q: What is the difference between prefix and postfix for `++` and `--`?
Prefix (`++x`): increment first, then use the new value. Postfix (`x++`): use the current value first, then increment.

### Q: What do the compound assignment operators `+=`, `-=`, `*=`, `/=`, `%=` do?
Each performs the operation and assigns the result to the left operand. Example: `z += x` is equivalent to `z = z + x`. Compound assignment can implicitly narrow (e.g. `byte b; b += 5` compiles).

### Q: How does short-circuit evaluation work for `&&` and `||`?
For `&&`, if the first operand is false, the second is not evaluated. For `||`, if the first operand is true, the second is not evaluated. This avoids unnecessary evaluation and can prevent errors (e.g. null checks).

### Q: What is the ternary operator syntax and meaning?
`condition ? valueIfTrue : valueIfFalse`. The condition is evaluated; if true the expression yields the value after `?`, otherwise the value after `:`.

### Q: What do the bitwise operators `&`, `|`, `^`, and `~` do?
`&` (AND): result bit 1 only if both bits 1. `|` (OR): result bit 1 if either bit 1. `^` (XOR): result bit 1 if bits differ. `~` (complement): inverts all bits (unary).

### Q: What do the left shift `<<` and right shift `>>` operators do?
`<<` shifts bits left, filling low-order bits with 0. `>>` shifts right, preserving sign (arithmetic right shift). Example: `8 << 2` is 32; `8 >> 2` is 2.

### Q: What is the range of the char type and how does char arithmetic work?
`char` is 16-bit unsigned (0 to 65,535), representing Unicode code units. In arithmetic (e.g. `'A' + 1`), char is promoted to int; the result is int (66). Cast back to char if needed: `(char)('A' + 1)`.

### Q: How does operator precedence affect an expression like `5 + 2 * 4`?
Multiplication has higher precedence than addition, so `2 * 4` is evaluated first (8), then `5 + 8` gives 13. Use parentheses to override: `(5 + 2) * 4` is 28.
