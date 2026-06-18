# Maximum Subarray - Detailed Explanation

## Problem Overview

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Example

```python
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6
```

Explanation:

The subarray

```python
[4,-1,2,1]
```

has the maximum sum:

```python
4 + (-1) + 2 + 1 = 6
```

---

## Understanding the Problem

We need to find a **continuous (contiguous) part** of the array whose sum is maximum.

- A subarray must contain adjacent elements.
- At least one element should be present.
- Elements can be positive, negative, or zero.

---

## Brute Force Idea

The straightforward approach is to generate every possible subarray and compute its sum.

For every starting index `i`, we extend the subarray till the end using index `j`, keeping track of the running sum.

Whenever a larger sum is found, we update the answer.

---

## Algorithm

1. Initialize:

```python
max_sum = nums[0]
```

2. Traverse all possible starting indices `i`.

3. For each `i`, initialize:

```python
current_sum = 0
```

4. Extend the subarray from `i` to `j`.

5. Add:

```python
current_sum += nums[j]
```

6. Update:

```python
max_sum = max(max_sum, current_sum)
```

7. Return `max_sum`.

---

## Python Code

```python
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]

        for i in range(len(nums)):
            current_sum = 0

            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum
```

---

## Dry Run

Input:

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

### Start

```python
max_sum = -2
```

### i = 0

Subarrays:

```
[-2]          sum = -2
[-2,1]        sum = -1
[-2,1,-3]     sum = -4
...
```

Current maximum:

```
1
```

---

### i = 3

Subarrays:

```
[4]           sum = 4
[4,-1]        sum = 3
[4,-1,2]      sum = 5
[4,-1,2,1]    sum = 6
```

Update:

```
max_sum = 6
```

---

### Remaining Iterations

No subarray produces a sum greater than 6.

Final answer:

```python
6
```

---

## Complexity Analysis

### Time Complexity

```
O(n²)
```

- Outer loop runs `n` times.
- Inner loop runs up to `n` times.
- All possible subarrays are examined.

### Space Complexity

```
O(1)
```

Only two variables (`max_sum` and `current_sum`) are used.

---

## Edge Cases Considered

### Single Element

```python
nums = [5]

Output = 5
```

---

### All Negative Numbers

```python
nums = [-4,-2,-7]

Output = -2
```

Maximum subarray:

```python
[-2]
```

---

### All Positive Numbers

```python
nums = [1,2,3]

Output = 6
```

Entire array becomes the answer.

---

### Array Containing Zero

```python
nums = [-2,0,-1]

Output = 0
```

Maximum subarray:

```python
[0]
```

---

## Pattern

- Array
- Brute Force
- Nested Loops

---

## Key Takeaway

> Generate every possible subarray by fixing a starting index and extending it to the right. Maintain a running sum and update the maximum sum whenever a larger value is found. Although simple, this approach takes O(n²) time and can be optimized to O(n) using Kadane's Algorithm.
