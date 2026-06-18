# Two Sum - Detailed Explanation

## Problem Overview

Given an array of integers `nums` and an integer `target`, find the indices of two numbers such that their sum equals the target.

### Example

```python
nums = [2, 7, 11, 15]
target = 9

Output: [0, 1]
```

Because:

```python
nums[0] + nums[1] = 2 + 7 = 9
```

---

## Understanding the Problem

We are not asked to return the numbers themselves, but their **indices**.

Conditions:

- Exactly one valid answer exists.
- The same element cannot be used twice.
- The order of indices does not matter.

---

## Brute Force Idea

The simplest approach is to check every possible pair of elements.

For each element, compare it with all the elements after it and see whether their sum equals the target.

### Visual Representation

```
nums = [2, 7, 11, 15]
target = 9

i = 0 → 2

    j = 1 → 7

    2 + 7 = 9 ✓

Return [0, 1]
```

---

## Algorithm

1. Start the outer loop with index `i`.
2. Start the inner loop from `i + 1`.
3. Check whether:

```python
nums[i] + nums[j] == target
```

4. If true, return `[i, j]`.
5. Continue until a pair is found.

---

## Code

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## Dry Run

### Input

```python
nums = [3, 2, 4]
target = 6
```

### Iteration 1

```
i = 0 (3)

j = 1 (2)

3 + 2 = 5 ✗
```

### Iteration 2

```
j = 2 (4)

3 + 4 = 7 ✗
```

### Iteration 3

```
i = 1 (2)

j = 2 (4)

2 + 4 = 6 ✓
```

Return:

```python
[1, 2]
```

---

## Why does j start from i + 1?

Suppose:

```python
nums = [3, 3]
target = 6
```

If both loops started from 0, the same element could be used twice.

Starting `j` from `i + 1` ensures:

- No duplicate pairs.
- No self-pairing.
- Every combination is checked exactly once.

---

## Complexity Analysis

### Time Complexity

```
O(n²)
```

Because two nested loops are used.

### Space Complexity

```
O(1)
```

No extra data structures are required.

---

## Edge Cases

### Duplicate Numbers

```python
nums = [3,3]
target = 6
```

Output:

```python
[0,1]
```

---

### Negative Numbers

```python
nums = [-1,-2,-3,-4,-5]
target = -8
```

Output:

```python
[2,4]
```

---

### Minimum Size Array

```python
nums = [1,2]
target = 3
```

Output:

```python
[0,1]
```

---

## Optimization

Brute force takes:

```
O(n²)
```

Using a HashMap, we can solve the problem in:

```
O(n)
```

by storing previously seen numbers and checking whether:

```python
target - nums[i]
```

already exists in the HashMap.

---

## Key Takeaway

> Brute force is easy to understand and implement, but pair-search problems can often be optimized using a HashMap. Whenever you need to answer "Have I already seen the value I need?", think of using a HashMap.
