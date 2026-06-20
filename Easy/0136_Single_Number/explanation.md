# Single Number - Detailed Explanation

## Problem Overview

Given a non-empty array of integers `nums`, every element appears twice except for one element that appears only once. Find that single element.

### Example

```python
Input: nums = [2,2,1]

Output: 1
```

```python
Input: nums = [4,1,2,1,2]

Output: 4
```

---

## Understanding the Problem

Most numbers occur exactly twice, and only one number occurs once.

Our task is to identify that unique number.

---

## Approach: Frequency Counting using Hash Map

We use a dictionary to count how many times each number appears.

### Step 1

Traverse the array and store the frequency of each number.

For example:

```python
nums = [4,1,2,1,2]
```

Dictionary becomes:

```python
{
    4:1,
    1:2,
    2:2
}
```

### Step 2

Traverse the dictionary and return the number whose frequency is 1.

Since only one element appears once, that element is the answer.

---

## Algorithm

1. Create an empty dictionary `count`.
2. Traverse each number in the array.
3. If the number already exists, increase its count.
4. Otherwise, insert it with count 1.
5. Traverse the dictionary.
6. Return the key whose value equals 1.

---

## Python Code

```python
class Solution:
    def singleNumber(self, nums):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] == 1:
                return num
```

---

## Dry Run

### Input

```python
nums = [4,1,2,1,2]
```

### First Loop

#### num = 4

```python
count = {4:1}
```

#### num = 1

```python
count = {4:1, 1:1}
```

#### num = 2

```python
count = {4:1, 1:1, 2:1}
```

#### num = 1

```python
count = {4:1, 1:2, 2:1}
```

#### num = 2

```python
count = {4:1, 1:2, 2:2}
```

---

### Second Loop

```
4 → count = 1 ✓
```

Return:

```python
4
```

---

## Why Hash Map Works

A dictionary allows us to store frequencies efficiently.

- First pass → count occurrences.
- Second pass → find the element with frequency 1.

This avoids repeatedly scanning the array.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

- First traversal: O(n)
- Second traversal: O(n)

Overall:

```
O(n)
```

---

### Space Complexity

```
O(n)
```

A dictionary is used to store frequencies.

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

### Negative Numbers

```python
nums = [-1,-1,-2]
```

Output:

```python
-2
```

---

### Zero Present

```python
nums = [0,1,1]
```

Output:

```python
0
```

---

### Unique Number at Beginning

```python
nums = [5,1,1,2,2]
```

Output:

```python
5
```

---

### Unique Number at End

```python
nums = [3,3,4]
```

Output:

```python
4
```

---

## Pattern

- Hash Map
- Frequency Counting
- Array

---

## Key Takeaway

> Whenever the problem asks to count occurrences or frequencies, a hash map (dictionary) is often a natural solution. By storing the frequency of each element, we can identify the unique element in linear time.
