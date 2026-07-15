# LeetCode 118 - Pascal's Triangle

## 📌 Problem Statement

Given an integer `numRows`, return the first `numRows` of Pascal's Triangle.

In Pascal's Triangle:

- The first and last element of every row is `1`.
- Every middle element is the sum of the two elements directly above it.

---

## Example

### Input
```text
numRows = 5
```

### Output
```text
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]
```

---

## Python Solution

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i - 1][j - 1] + result[i - 1][j])

            result.append(row)

        return result
```

---

## Approach

1. Create an empty list `result` to store all rows.
2. Iterate from `0` to `numRows - 1`.
3. For each row:
   - Add `1` at the beginning and end.
   - For the middle elements, use:
     ```python
     result[i-1][j-1] + result[i-1][j]
     ```
4. Append the row to `result`.
5. Return `result`.

---

## Dry Run

### Input

```text
numRows = 5
```

### Step 1

```text
[1]
```

### Step 2

```text
[1,1]
```

### Step 3

```text
[1,2,1]
```

### Step 4

```text
[1,3,3,1]
```

### Step 5

```text
[1,4,6,4,1]
```

Final Output:

```text
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]
```

---

## Complexity Analysis

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n²)`

---

## Key Takeaways

- The first and last element of every row is always `1`.
- Each middle element is the sum of the two elements directly above it.
- The solution uses the previous row to build the current row.

---

⭐ **LeetCode Problem:** 118 - Pascal's Triangle
