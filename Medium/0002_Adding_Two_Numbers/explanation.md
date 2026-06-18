# Add Two Numbers - Detailed Explanation

## Problem Overview

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

### Example

```
l1 = [2,4,3]
l2 = [5,6,4]

342 + 465 = 807

Output = [7,0,8]
```

---

## Understanding the Problem

Each linked list stores digits in reverse order:

```
2 → 4 → 3 represents 342
5 → 6 → 4 represents 465
```

We need to add corresponding digits just like elementary addition, keeping track of the carry.

---

## Approach

To simplify the construction of the answer linked list, we use a **dummy node**.

At each iteration:

1. Take the current digit from both lists.
2. If a list has ended, use 0.
3. Add the two digits and the carry.
4. Store the one's place digit in the result list.
5. Update the carry with the ten's place digit.
6. Move to the next nodes.

Continue until:

- Both lists are exhausted.
- No carry remains.

---

## Algorithm

1. Create a dummy node.
2. Initialize:

```python
curr = dummy
carry = 0
```

3. Repeat while:

```python
l1 or l2 or carry
```

4. Extract current values:

```python
x = l1.val if l1 else 0
y = l2.val if l2 else 0
```

5. Calculate:

```python
total = x + y + carry
```

6. Update carry:

```python
carry = total // 10
```

7. Create new node:

```python
curr.next = ListNode(total % 10)
```

8. Move all pointers forward.

9. Return:

```python
dummy.next
```

---

## Python Code

```python
def addTwoNumbers(self, l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        carry = total // 10

        curr.next = ListNode(total % 10)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next
```

---

## Dry Run

### Input

```
l1 = 2 → 4 → 3
l2 = 5 → 6 → 4
```

### Iteration 1

```
2 + 5 + 0 = 7

Digit = 7
Carry = 0
```

Result:

```
7
```

---

### Iteration 2

```
4 + 6 + 0 = 10

Digit = 0
Carry = 1
```

Result:

```
7 → 0
```

---

### Iteration 3

```
3 + 4 + 1 = 8

Digit = 8
Carry = 0
```

Result:

```
7 → 0 → 8
```

Output:

```
[7,0,8]
```

---

## Why Use a Dummy Node?

Without a dummy node, special handling is required for the first node.

The dummy node allows us to:

- Build the answer uniformly.
- Avoid checking whether the head exists.
- Return the answer simply using:

```python
dummy.next
```

---

## Complexity Analysis

### Time Complexity

```
O(max(m,n))
```

where:

- m = length of l1
- n = length of l2

Each node is visited exactly once.

### Space Complexity

```
O(max(m,n))
```

A new linked list is created to store the answer.

---

## Edge Cases Considered

### Different Length Lists

```
l1 = [9,9,9]
l2 = [1]

Output = [0,0,0,1]
```

---

### Final Carry Exists

```
9 + 1 = 10
```

Carry creates an extra node.

---

### One List is Shorter

Missing digits are treated as 0:

```python
x = l1.val if l1 else 0
y = l2.val if l2 else 0
```

---

## Pattern

- Linked List
- Simulation
- Carry Propagation
- Dummy Node

---

## Key Takeaway

> Whenever a linked list needs to be constructed node by node, using a dummy node simplifies the implementation. Carry propagation works exactly like elementary addition and allows us to process lists of different lengths efficiently.
