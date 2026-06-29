# Squares of a Sorted Array - Detailed Explanation

## Problem Overview

Given an integer array `nums` sorted in non-decreasing order, return an array containing the squares of each number, also sorted in non-decreasing order.

### Example

```python
Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]
```

### Another Example

```python
Input: nums = [-7,-3,2,3,11]

Output: [4,9,9,49,121]
```

---

## Understanding the Problem

Although the input array is already sorted, squaring negative numbers changes their order.

For example:

```python
nums = [-4,-2,3]
```

Squaring each element gives:

```python
[16,4,9]
```

This is **not sorted**, so we need to sort the squared values before returning them.

---

## Approach: Map + Lambda + Sorting

This solution uses two built-in Python functions:

- **`map()`** applies a function to every element in the array.
- **`lambda`** defines an anonymous function that squares each number.
- **`sorted()`** sorts the squared values in ascending order.

The process is:

1. Square every element using `map()` and `lambda`.
2. Sort the resulting squared values using `sorted()`.
3. Return the sorted list.

---

## Algorithm

1. Traverse the array using `map()`.
2. Square each element using:

```python
lambda x: x * x
```

3. Sort all squared values using `sorted()`.
4. Return the sorted array.

---

## Python Code

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x * x, nums))
```

---

## Dry Run

### Input

```python
nums = [-4,-1,0,3,10]
```

### Step 1: Square Every Element

```
-4 → 16
-1 → 1
 0 → 0
 3 → 9
10 → 100
```

Result after `map()`:

```python
[16,1,0,9,100]
```

---

### Step 2: Sort

```python
sorted([16,1,0,9,100])
```

Result:

```python
[0,1,9,16,100]
```

Return:

```python
[0,1,9,16,100]
```

---

## Why `map()` and `lambda`?

The expression

```python
map(lambda x: x * x, nums)
```

means:

- Take every element in `nums`.
- Square it.
- Produce an iterable of squared values.

Then,

```python
sorted(...)
```

arranges those squared values in ascending order.

This provides a short and clean implementation.

---

## Complexity Analysis

### Time Complexity

```
O(n log n)
```

- Squaring all elements using `map()` takes **O(n)**.
- Sorting the squared values takes **O(n log n)**.

Overall:

```
O(n log n)
```

---

### Space Complexity

```
O(n)
```

A new list is created to store the squared values.

---

## Edge Cases Considered

### All Positive Numbers

```python
nums = [1,2,3]
```

Output:

```python
[1,4,9]
```

---

### All Negative Numbers

```python
nums = [-5,-3,-1]
```

Output:

```python
[1,9,25]
```

---

### Mixed Positive and Negative Numbers

```python
nums = [-4,-1,0,3,10]
```

Output:

```python
[0,1,9,16,100]
```

---

### Contains Zero

```python
nums = [0]
```

Output:

```python
[0]
```

---

### Duplicate Values

```python
nums = [-2,-2,2]
```

Output:

```python
[4,4,4]
```

---

## Pattern

- Array
- Sorting
- Functional Programming
- `map()`
- `lambda`

---

## Key Takeaway

> Python's `map()` function combined with a `lambda` expression provides a concise way to transform every element in a collection. Since squaring negative numbers can change their relative order, sorting the squared values is necessary to produce the final result. This solution is simple, readable, and runs in **O(n log n)** time.
