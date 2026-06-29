# Search Insert Position - Detailed Explanation

## Problem Overview

Given a sorted array of distinct integers `nums` and a target value `target`, return the index if the target is found.

If the target is not present, return the index where it should be inserted so that the array remains sorted.

### Example

```python
Input: nums = [1,3,5,6], target = 5

Output: 2
```

```python
Input: nums = [1,3,5,6], target = 2

Output: 1
```

---

## Understanding the Problem

The array is already sorted.

If the target exists, return its index.

If it does not exist, determine the correct position where it can be inserted while maintaining the sorted order.

Since the array is sorted, **Binary Search** is the most efficient approach.

---

## Approach: Binary Search

Binary Search repeatedly divides the search space into two halves.

- If the middle element equals the target, return its index.
- If the middle element is smaller than the target, search in the right half.
- Otherwise, search in the left half.

If the target is not found, the `left` pointer will indicate the correct insertion position.

---

## Algorithm

1. Initialize two pointers:
   - `left = 0`
   - `right = len(nums) - 1`
2. While `left <= right`:
   - Calculate the middle index.
   - If the middle element equals the target, return its index.
   - If the middle element is smaller than the target, move `left` to `mid + 1`.
   - Otherwise, move `right` to `mid - 1`.
3. If the loop ends without finding the target, return `left` as the insertion position.

---

## Python Code

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

---

## Dry Run

### Input

```python
nums = [1,3,5,6]
target = 2
```

### Initial Values

```
left = 0
right = 3
```

### Iteration 1

```
mid = (0 + 3) // 2 = 1

nums[mid] = 3
```

Since:

```
3 > 2
```

Move:

```
right = mid - 1 = 0
```

---

### Iteration 2

```
left = 0
right = 0

mid = 0

nums[mid] = 1
```

Since:

```
1 < 2
```

Move:

```
left = mid + 1 = 1
```

Now:

```
left = 1
right = 0
```

The loop ends.

Return:

```python
left = 1
```

The target should be inserted at index **1**.

---

## Why Return `left`?

When Binary Search ends without finding the target:

```
left > right
```

At this point, `left` points to the first position where the target can be inserted without disturbing the sorted order.

Example:

```
nums = [1,3,5,6]
target = 4
```

Loop ends with:

```
left = 2
right = 1
```

Insert at index:

```
2
```

Result:

```
[1,3,4,5,6]
```

---

## Complexity Analysis

### Time Complexity

```
O(log n)
```

The search space is halved in every iteration.

---

### Space Complexity

```
O(1)
```

Only a few variables (`left`, `right`, and `mid`) are used, regardless of the input size.

---

## Edge Cases Considered

### Target Exists

```python
nums = [1,3,5,6]
target = 5
```

Output:

```python
2
```

---

### Insert at Beginning

```python
nums = [2,4,6]
target = 1
```

Output:

```python
0
```

---

### Insert at End

```python
nums = [1,3,5]
target = 7
```

Output:

```python
3
```

---

### Insert in Middle

```python
nums = [1,3,5,6]
target = 4
```

Output:

```python
2
```

---

### Single Element Array

```python
nums = [1]
target = 0
```

Output:

```python
0
```

---

## Pattern

- Binary Search
- Array
- Divide and Conquer

---

## Key Takeaway

> Whenever a problem involves searching in a sorted array, Binary Search is often the optimal solution. Even if the target is not found, the final value of the `left` pointer naturally gives the correct insertion position, making the solution both simple and efficient with **O(log n)** time complexity.
