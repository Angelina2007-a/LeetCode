# Reverse Integer - Detailed Explanation

## Problem Overview

Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range

```
[-2³¹, 2³¹ - 1]
```

then return `0`.

### Example

```python
Input: x = 123

Output: 321
```

```python
Input: x = -123

Output: -321
```

```python
Input: x = 120

Output: 21
```

---

## Understanding the Problem

We need to reverse the digits of the integer while preserving its sign.

Examples:

```python
123  -> 321
-456 -> -654
120  -> 21
```

If the reversed number exceeds the 32-bit signed integer range, the answer should be `0`.

---

## Approach: String Reversal

The easiest way is to convert the integer into a string and reverse it using slicing.

For positive numbers:

- Convert to string.
- Reverse the string using `[::-1]`.
- Convert it back to integer.

For negative numbers:

- Remove the sign.
- Reverse the digits.
- Add the negative sign back.

Finally, check whether the reversed integer lies within the 32-bit signed integer range.

---

## Algorithm

1. If `x` is negative:
   - Remove the negative sign.
   - Reverse the digits.
   - Add the sign back.
2. Otherwise, reverse the digits directly.
3. Check whether the reversed integer lies within:

```python
-2**31 <= rev <= 2**31 - 1
```

4. If not, return `0`.
5. Otherwise, return the reversed number.

---

## Python Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev = -int(str(-x)[::-1])
        else:
            rev = int(str(x)[::-1])

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        else:
            return rev
```

---

## Dry Run

### Input

```python
x = -123
```

Since x is negative:

```python
str(-x) = "123"
```

Reverse:

```python
"123"[::-1] = "321"
```

Add sign back:

```python
rev = -321
```

Range check:

```python
-2³¹ ≤ -321 ≤ 2³¹ -1
```

Valid.

Return:

```python
-321
```

---

## Another Example

### Input

```python
x = 120
```

Convert to string:

```python
"120"
```

Reverse:

```python
"021"
```

Convert to integer:

```python
21
```

Return:

```python
21
```

---

## Why String Reversal Works

Python's slicing operator

```python
[::-1]
```

efficiently reverses the string representation of the number.

Handling negative numbers separately preserves the sign.

---

## Complexity Analysis

### Time Complexity

```
O(d)
```

where `d` is the number of digits.

Reversing a string of length `d` takes linear time.

---

### Space Complexity

```
O(d)
```

because a new reversed string is created.

---

## Edge Cases Considered

### Positive Number

```python
Input: 123

Output: 321
```

---

### Negative Number

```python
Input: -456

Output: -654
```

---

### Number Ending With Zero

```python
Input: 120

Output: 21
```

Leading zeros disappear after converting back to integer.

---

### Zero

```python
Input: 0

Output: 0
```

---

### Overflow Case

```python
Input: 1534236469
```

Reversed number exceeds:

```python
2³¹ - 1
```

Output:

```python
0
```

---

## Pattern

- Math
- String Manipulation
- Simulation

---

## Key Takeaway

> Converting an integer to a string and reversing it with slicing provides a simple solution. Always perform a range check afterward because the reversed value may exceed the 32-bit signed integer limit.
