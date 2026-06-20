# Majority Element - Detailed Explanation

## Problem Overview

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.

You may assume that the majority element always exists in the array.

### Example

```python
Input: nums = [3,2,3]

Output: 3
```

```python
Input: nums = [2,2,1,1,1,2,2]

Output: 2
```

---

## Understanding the Problem

Among all the numbers in the array, one number appears more than half the size of the array.

Our task is to identify that number.

---

## Approach: Frequency Counting using Hash Map

We use a dictionary to count the number of occurrences of each element.

### Step 1

Traverse the array and store the frequency of every number.

For example:

```python
nums = [2,2,1,1,1,2,2]
```

Dictionary becomes:

```python
{
    2:4,
    1:3
}
```

### Step 2

Find the maximum frequency.

```python
maximum = max(count.values())
```

### Step 3

Traverse the dictionary and return the element whose frequency equals the maximum frequency.

Since the majority element always exists, that element is guaranteed to be the answer.

---

## Algorithm

1. Create an empty dictionary `count`.
2. Traverse the array.
3. Increase the frequency of each element.
4. Find the maximum frequency.
5. Traverse the dictionary again.
6. Return the element whose count equals the maximum frequency.

---

## Python Code

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        maximum = max(count.values())

        for num in count:
            if count[num] == maximum:
                return num
```

---

## Dry Run

### Input

```python
nums = [2,2,1,1,1,2,2]
```

### First Loop

#### num = 2

```python
count = {2:1}
```

#### num = 2

```python
count = {2:2}
```

#### num = 1

```python
count = {2:2,1:1}
```

#### num = 1

```python
count = {2:2,1:2}
```

#### num = 1

```python
count = {2:2,1:3}
```

#### num = 2

```python
count = {2:3,1:3}
```

#### num = 2

```python
count = {2:4,1:3}
```

---

### Find Maximum Frequency

```python
maximum = 4
```

Traverse the dictionary:

```
2 → count = 4 ✓
```

Return:

```python
2
```

---

## Why Hash Map Works

The dictionary stores the frequency of each element efficiently.

By counting occurrences first and then finding the maximum count, we can easily determine the majority element.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

- First traversal to build the dictionary → O(n)
- Finding maximum frequency → O(n)
- Second traversal through dictionary → O(n)

Overall:

```
O(n)
```

---

### Space Complexity

```
O(n)
```

In the worst case, all elements are distinct, requiring a dictionary of size n.

---

## Edge Cases Considered

### Single Element

```python
nums = [1]
```

Output:

```python
1
```

---

### Majority Element Appears Everywhere

```python
nums = [5,5,5,5]
```

Output:

```python
5
```

---

### Negative Numbers

```python
nums = [-1,-1,-1,2,3]
```

Output:

```python
-1
```

---

### Majority Element at the End

```python
nums = [1,2,3,3,3]
```

Output:

```python
3
```

---

## Pattern

- Hash Map
- Frequency Counting
- Array

---

## Key Takeaway

> Whenever a problem asks for the most frequent element, a hash map is a straightforward approach. By storing the frequency of each element, we can efficiently identify the majority element in linear time.
