# Valid Parentheses - Detailed Explanation

## Problem Overview

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

A string is considered valid if:

- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every closing bracket has a corresponding opening bracket.

### Example

```python
Input: s = "()[]{}"

Output: True
```

```python
Input: s = "(]"

Output: False
```

---

## Understanding the Problem

Whenever an opening bracket appears, we expect a matching closing bracket later.

Since the most recently opened bracket should be closed first, this follows the **Last In First Out (LIFO)** principle, making a stack the ideal data structure.

---

## Approach: Stack

Instead of storing opening brackets, we store the expected closing brackets.

For each character:

- If it is an opening bracket, push its matching closing bracket onto the stack.
- If it is a closing bracket, compare it with the top of the stack.
- If they don't match or the stack is empty, return `False`.
- At the end, if the stack is empty, all brackets were matched correctly.

---

## Algorithm

1. Create an empty stack.
2. Traverse each character in the string.
3. If the character is:
   - `'('`, push `')'`
   - `'['`, push `']'`
   - `'{'`, push `'}'`
4. Otherwise, the character is a closing bracket:
   - If the stack is empty or the top element doesn't match, return `False`.
5. After processing all characters, return `True` only if the stack is empty.

---

## Python Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            elif not stack or stack.pop() != ch:
                return False

        return not stack
```

---

## Dry Run

### Input

```python
s = "([{}])"
```

### Step 1

```
Character = '('

Stack = [')']
```

### Step 2

```
Character = '['

Stack = [')', ']']
```

### Step 3

```
Character = '{'

Stack = [')', ']', '}']
```

### Step 4

```
Character = '}'

Top of stack = '}'

Match ✓

Stack = [')', ']']
```

### Step 5

```
Character = ']'

Top = ']'

Match ✓

Stack = [')']
```

### Step 6

```
Character = ')'

Top = ')'

Match ✓

Stack = []
```

Since the stack is empty, return:

```python
True
```

---

## Why Store Closing Brackets?

Instead of storing opening brackets and checking mappings later, we directly store the expected closing bracket.

For example:

```
Input = "({"
```

Stack becomes:

```
[')', '}']
```

When `}` appears, we simply pop and compare.

This makes the code shorter and easier to understand.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

Each character is pushed and popped at most once.

### Space Complexity

```
O(n)
```

In the worst case, all characters are opening brackets and are stored in the stack.

---

## Edge Cases Considered

### Empty String

```python
s = ""
```

Output:

```python
True
```

---

### Single Opening Bracket

```python
s = "("
```

Output:

```python
False
```

---

### Mismatched Brackets

```python
s = "(]"
```

Output:

```python
False
```

---

### Incorrect Order

```python
s = "([)]"
```

Output:

```python
False
```

---

### Nested Brackets

```python
s = "{[]}"
```

Output:

```python
True
```

---

## Pattern

- Stack
- String
- LIFO (Last In First Out)

---

## Key Takeaway

> Whenever the problem requires matching pairs and the most recently added element should be processed first, think of a stack. Storing the expected closing brackets directly simplifies the implementation and makes bracket validation efficient with O(n) time complexity.
