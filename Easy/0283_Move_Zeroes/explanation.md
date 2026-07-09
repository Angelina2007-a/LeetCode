# Move Zeroes - Detailed Explanation

## Problem Overview

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The operation must be performed **in-place**, without creating another array.

### Example

```python
Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]
```

---

## Understanding the Problem

We need to rearrange the array such that:

- All non-zero elements remain in their original order.
- All zeros are shifted to the end.
- The modification should be done in-place.

---

## Approach: Two Pointers

Use two pointers:

- `i` traverses every element in the array.
- `j` keeps track of the position where the next non-zero element should be placed.

Whenever a non-zero element is found:

- Swap it with the element at index `j`.
- Increment `j`.

By the end of the traversal, all non-zero elements are placed at the beginning, and the remaining positions naturally contain zeros.

---

## Algorithm

1. Initialize `j = 0`.
2. Traverse the array using index `i`.
3. If `nums[i]` is not zero:
   - Swap `nums[i]` and `nums[j]`.
   - Increment `j`.
4. Continue until the end of the array.
5. The array is modified in-place.

---

## Python Code

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
```

---

## Dry Run

### Input

```python
nums = [0,1,0,3,12]
```

Initial:

```
j = 0
```

### Iteration 1

```
i = 0

nums[i] = 0

Skip
```

Array:

```
[0,1,0,3,12]
```

---

### Iteration 2

```
i = 1

nums[i] = 1
```

Swap:

```
nums[0] ↔ nums[1]
```

Array:

```
[1,0,0,3,12]
```

```
j = 1
```

---

### Iteration 3

```
i = 2

nums[i] = 0

Skip
```

---

### Iteration 4

```
i = 3

nums[i] = 3
```

Swap:

```
nums[1] ↔ nums[3]
```

Array:

```
[1,3,0,0,12]
```

```
j = 2
```

---

### Iteration 5

```
i = 4

nums[i] = 12
```

Swap:

```
nums[2] ↔ nums[4]
```

Array:

```
[1,3,12,0,0]
```

```
j = 3
```

Final Output:

```python
[1,3,12,0,0]
```

---

## Why Two Pointers?

The pointer `j` always indicates the position where the next non-zero element should be placed.

The pointer `i` scans the array.

Whenever a non-zero element is found, it is moved to its correct position while preserving the order of previously encountered non-zero elements.

---

## Pattern

- Two Pointers
- Array
- In-place Modification

---

## Key Takeaway

> The Two Pointers technique efficiently moves all non-zero elements to the front of the array while maintaining their relative order. Since the array is modified in-place without using an additional array, the solution is both space-efficient and optimal.
