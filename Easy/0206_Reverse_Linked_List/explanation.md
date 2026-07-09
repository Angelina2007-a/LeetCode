# Reverse Linked List - Detailed Explanation

## Problem Overview

Given the head of a singly linked list, reverse the list and return the new head.

### Example

```text
Input:

1 → 2 → 3 → 4 → 5

Output:

5 → 4 → 3 → 2 → 1
```

---

## Understanding the Problem

Each node in a singly linked list points to the next node.

To reverse the list, every node should point to its previous node instead of the next one.

For example,

Before reversing:

```text
1 → 2 → 3 → 4 → 5 → null
```

After reversing:

```text
5 → 4 → 3 → 2 → 1 → null
```

---

## Approach: Iterative Method

Use three pointers:

- `prev` → Stores the previous node.
- `curr` → Points to the current node being processed.
- `next` → Temporarily stores the next node before changing the link.

For every node:

1. Store the next node.
2. Reverse the current node's link.
3. Move `prev` one step ahead.
4. Move `curr` one step ahead.

Repeat until all nodes are processed.

---

## Algorithm

1. Initialize:
   - `prev = null`
   - `curr = head`
2. While `curr` is not `null`:
   - Store `curr.next` in `next`.
   - Point `curr.next` to `prev`.
   - Move `prev` to `curr`.
   - Move `curr` to `next`.
3. Return `prev` as the new head of the reversed list.

---

## Java Code

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}
```

---

## Dry Run

### Input

```text
1 → 2 → 3 → null
```

### Initial State

```
prev = null
curr = 1
```

---

### Iteration 1

```
next = 2

1 → null

prev = 1
curr = 2
```

Current list:

```text
1 → null

Remaining:

2 → 3
```

---

### Iteration 2

```
next = 3

2 → 1 → null

prev = 2
curr = 3
```

---

### Iteration 3

```
next = null

3 → 2 → 1 → null

prev = 3
curr = null
```

Loop ends.

Return:

```text
3 → 2 → 1 → null
```

---

## Why Three Pointers?

If we directly reverse the pointer without storing the next node, the remaining part of the linked list would be lost.

The `next` pointer safely stores the remaining list before changing the links.

---

## Pattern

- Linked List
- Iterative Traversal
- Pointer Manipulation

---

## Key Takeaway

> Reversing a linked list can be done efficiently using three pointers (`prev`, `curr`, and `next`). By reversing one link at a time while preserving the next node, the entire list can be reversed in a single traversal with constant extra space.
