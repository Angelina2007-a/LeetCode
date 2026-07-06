# 3Sum - Detailed Explanation

## Problem Overview

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

### Example

```python
Input: nums = [-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],[-1,0,1]]
```

---

## Understanding the Problem

We need to find every unique combination of **three numbers** whose sum equals **0**.

Since duplicate triplets are not allowed, we must carefully avoid processing the same values multiple times.

To efficiently solve the problem, we first sort the array and then use the **Two Pointers** technique.

---

## Approach: Sorting + Two Pointers

1. Sort the array.
2. Fix one element at a time using index `i`.
3. Use two pointers:
   - `left` starts just after `i`.
   - `right` starts from the end of the array.
4. Calculate the sum of the three numbers.
5. If the sum is:
   - **0** → Store the triplet.
   - **Less than 0** → Move `left` to increase the sum.
   - **Greater than 0** → Move `right` to decrease the sum.
6. Skip duplicate values to avoid repeated triplets.

---

## Algorithm

1. Sort the array.
2. Traverse the array using index `i`.
3. Skip duplicate values of `nums[i]`.
4. Initialize:
   - `left = i + 1`
   - `right = len(nums) - 1`
5. While `left < right`:
   - Compute the sum of the three numbers.
   - If the sum is 0:
     - Add the triplet to the result.
     - Move both pointers.
     - Skip duplicate values.
   - If the sum is less than 0:
     - Move `left` forward.
   - Otherwise:
     - Move `right` backward.
6. Return the result list.

---

## Python Code

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
```

---

## Dry Run

### Input

```python
nums = [-1,0,1,2,-1,-4]
```

### Step 1: Sort

```python
[-4,-1,-1,0,1,2]
```

---

### i = 0

```
nums[i] = -4

left = 1
right = 5
```

```
-4 + (-1) + 2 = -3
```

Too small.

Move `left`.

Continue until `left == right`.

No triplet found.

---

### i = 1

```
nums[i] = -1

left = 2
right = 5
```

```
-1 + (-1) + 2 = 0
```

Triplet found:

```python
[-1,-1,2]
```

Move both pointers.

---

Now:

```
left = 3
right = 4
```

```
-1 + 0 + 1 = 0
```

Triplet found:

```python
[-1,0,1]
```

Move pointers.

Loop ends.

---

### i = 2

Duplicate value:

```
nums[2] == nums[1]
```

Skip it.

---

Final Answer

```python
[
 [-1,-1,2],
 [-1,0,1]
]
```

---

## Why Sort the Array?

Sorting makes it possible to use the **Two Pointers** technique.

- If the sum is too small, moving the left pointer increases the sum.
- If the sum is too large, moving the right pointer decreases the sum.

Without sorting, this strategy would not work.

---

## Why Skip Duplicates?

Consider:

```python
[-1,-1,-1,2]
```

Without skipping duplicates, the same triplet would be added multiple times.

These conditions prevent duplicate results:

```python
if i > 0 and nums[i] == nums[i-1]:
    continue
```

and

```python
while left < right and nums[left] == nums[left-1]:
    left += 1
```

---

## Complexity Analysis

### Time Complexity

```
O(n²)
```

- Sorting the array takes **O(n log n)**.
- The outer loop runs **O(n)** times.
- The two pointers traverse the remaining array in **O(n)** time.

Overall:

```
O(n²)
```

---

### Space Complexity

```
O(1)
```

Ignoring the output list, only a few variables (`left`, `right`, and `total`) are used.

If the output list is included, the space complexity becomes **O(k)**, where **k** is the number of valid triplets.

---

## Edge Cases Considered

### Empty Array

```python
nums = []
```

Output:

```python
[]
```

---

### Less Than Three Elements

```python
nums = [1,2]
```

Output:

```python
[]
```

---

### No Valid Triplets

```python
nums = [1,2,3]
```

Output:

```python
[]
```

---

### Duplicate Numbers

```python
nums = [-1,-1,-1,2,2]
```

Output:

```python
[[-1,-1,2]]
```

Only one unique triplet is returned.

---

### All Zeros

```python
nums = [0,0,0,0]
```

Output:

```python
[[0,0,0]]
```

Duplicate triplets are avoided.

---

### Mixed Positive and Negative Numbers

```python
nums = [-2,0,1,1,2]
```

Output:

```python
[[-2,0,2],[-2,1,1]]
```

---

## Pattern

- Sorting
- Two Pointers
- Array
- Duplicate Handling

---

## Key Takeaway

> Sorting the array allows us to efficiently use the Two Pointers technique to find triplets whose sum is zero. By skipping duplicate values for the fixed element and the moving pointers, we ensure that every valid triplet appears exactly once. This approach improves the brute-force solution from **O(n³)** to **O(n²)**.
