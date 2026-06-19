# Longest Substring Without Repeating Characters - Detailed Explanation

## Problem Overview

Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters.

### Example

```python
Input: s = "abcabcbb"

Output: 3
```

Explanation:

The longest substring without repeating characters is:

```python
"abc"
```

whose length is 3.

---

## Understanding the Problem

We need to find the maximum length of a contiguous substring such that no character appears more than once.

For example:

```python
s = "pwwkew"
```

Valid substrings:

```
"pw"
"wke"
"kew"
```

Longest length = 3.

---

## Approach: Sliding Window + Hash Set

Instead of checking all possible substrings, we maintain a sliding window using two pointers.

- `left` represents the start of the window.
- `i` represents the end of the window.
- A set stores the characters currently inside the window.

Whenever a duplicate character is encountered, we shrink the window from the left until the duplicate is removed. Then we add the current character and update the maximum length.

---

## Algorithm

1. Initialize an empty set.
2. Set `left = 0`.
3. Traverse the string using index `i`.
4. If the current character already exists in the set:
   - Remove characters from the left side.
   - Move `left` forward until the duplicate disappears.
5. Add the current character to the set.
6. Update the maximum length.
7. Return the maximum length.

---

## Python Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        left = 0
        max_len = 0

        for i in range(len(s)):
            while s[i] in count:
                count.remove(s[left])
                left += 1

            count.add(s[i])

            max_len = max(max_len, i - left + 1)

        return max_len
```

---

## Dry Run

### Input

```python
s = "abcabcbb"
```

### i = 0

```
Window = "a"

Set = {a}

max_len = 1
```

### i = 1

```
Window = "ab"

Set = {a,b}

max_len = 2
```

### i = 2

```
Window = "abc"

Set = {a,b,c}

max_len = 3
```

### i = 3

Current character = 'a'

'a' already exists.

Remove from left:

```
Remove 'a'

Window becomes "bca"
```

Set = {b,c,a}

max_len = 3

Continue similarly.

Final Answer:

```python
3
```

---

## Why Sliding Window Works

The window always contains unique characters.

Whenever a duplicate appears, we move the left pointer until the duplicate is removed.

Thus, every character enters and leaves the window at most once.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

Each character is added and removed from the set at most once.

### Space Complexity

```
O(min(n, m))
```

where:

- `n` = length of string
- `m` = size of character set

The set stores only unique characters in the current window.

---

## Edge Cases Considered

### Empty String

```python
s = ""
```

Output:

```python
0
```

---

### Single Character

```python
s = "a"
```

Output:

```python
1
```

---

### All Characters Same

```python
s = "aaaa"
```

Output:

```python
1
```

---

### All Characters Unique

```python
s = "abcdef"
```

Output:

```python
6
```

---

### Duplicate Characters in Between

```python
s = "pwwkew"
```

Longest substring:

```python
"wke"
```

Output:

```python
3
```

---

## Pattern

- Sliding Window
- Two Pointers
- Hash Set
- String

---

## Key Takeaway

> Whenever we need to find the longest or shortest contiguous segment satisfying some condition, think of the Sliding Window technique. A Hash Set helps us efficiently detect duplicate characters, allowing the solution to run in O(n) time.
