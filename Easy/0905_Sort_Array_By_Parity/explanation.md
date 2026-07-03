# Sort Array By Parity - Detailed Explanation

## Problem Overview

Given an integer array `nums`, move all the even integers to the beginning of the array, followed by all the odd integers.

The relative order among even or odd numbers does not matter.

### Example

```python
Input: nums = [3,1,2,4]

Output: [2,4,3,1]
```

Another valid output could be:

```python
[4,2,1,3]
```

---

## Understanding the Problem

We need to rearrange the array so that:

- All **even** numbers come first.
- All **odd** numbers come after the even numbers.

The order within the even and odd groups is not important.

---

## Approach: Two Traversals

This solution creates a new list named `res`.

- In the first traversal, it collects all the even numbers.
- In the second traversal, it collects all the odd numbers.

Finally, the resulting list contains all even numbers followed by all odd numbers.

---

## Algorithm

1. Create an empty list `res`.
2. Traverse the array.
3. If a number is even, append it to `res`.
4. Traverse the array again.
5. If a number is odd, append it to `res`.
6. Return the resulting list.

---

## Python Code

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []

        # Add even numbers
        for num in nums:
            if num % 2 == 0:
                res.append(num)

        # Add odd numbers
        for num in nums:
            if num % 2 != 0:
                res.append(num)

        return res
```

---

## Dry Run

### Input

```python
nums = [3,1,2,4]
```

### First Traversal (Even Numbers)

```
3 → Odd → Skip
1 → Odd → Skip
2 → Even → Append
4 → Even → Append
```

Result:

```python
res = [2,4]
```

---

### Second Traversal (Odd Numbers)

```
3 → Odd → Append
1 → Odd → Append
2 → Even → Skip
4 → Even → Skip
```

Final Result:

```python
res = [2,4,3,1]
```

Return:

```python
[2,4,3,1]
```

---

## Why Two Traversals?

Using two separate traversals keeps the solution simple and easy to understand.

- The first loop collects all even numbers.
- The second loop appends all odd numbers.

This guarantees that every even number appears before every odd number.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

- The first loop traverses the array once → **O(n)**
- The second loop traverses the array once → **O(n)**

Overall:

```
O(n)
```

---

### Space Complexity

```
O(n)
```

A new list `res` is created to store the reordered elements.

---

## Edge Cases Considered

### All Even Numbers

```python
nums = [2,4,6,8]
```

Output:

```python
[2,4,6,8]
```

---

### All Odd Numbers

```python
nums = [1,3,5,7]
```

Output:

```python
[1,3,5,7]
```

---

### Mixed Even and Odd Numbers

```python
nums = [3,1,2,4]
```

Output:

```python
[2,4,3,1]
```

---

### Single Element (Even)

```python
nums = [8]
```

Output:

```python
[8]
```

---

### Single Element (Odd)

```python
nums = [5]
```

Output:

```python
[5]
```

---

### Contains Zero

```python
nums = [0,1,2]
```

Output:

```python
[0,2,1]
```

Since `0` is an even number, it appears in the even section.

---

### Empty Array

```python
nums = []
```

Output:

```python
[]
```

The algorithm correctly returns an empty list.

---

## Pattern

- Array
- Traversal
- Simulation

---

## Key Takeaway

> A simple way to group elements based on a condition is to perform separate traversals for each category. In this problem, collecting all even numbers first and then all odd numbers produces the required arrangement in **O(n)** time while using an additional result list.
