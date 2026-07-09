# Best Time to Buy and Sell Stock - Detailed Explanation

## Problem Overview

You are given an array `prices`, where `prices[i]` represents the price of a stock on the `iᵗʰ` day.

You want to maximize your profit by choosing:

- One day to buy the stock.
- A later day to sell the stock.

Return the maximum profit you can achieve.

If no profit is possible, return `0`.

### Example

```java
Input: prices = [7,1,5,3,6,4]

Output: 5
```

Explanation:

- Buy on Day 2 at price **1**.
- Sell on Day 5 at price **6**.
- Profit = **6 - 1 = 5**

---

## Understanding the Problem

We can buy the stock only once and sell it only once.

To maximize profit:

- Always buy at the **lowest price seen so far**.
- For each day's price, calculate the profit if sold on that day.
- Keep track of the maximum profit found.

---

## Approach: Single Traversal

Maintain two variables:

- `minPrice` → Lowest stock price encountered so far.
- `maxProfit` → Maximum profit obtained so far.

For each price:

- If the current price is lower than `minPrice`, update `minPrice`.
- Otherwise, calculate the profit by selling today.
- Update `maxProfit` if this profit is greater.

---

## Algorithm

1. Initialize:
   - `minPrice = Integer.MAX_VALUE`
   - `maxProfit = 0`
2. Traverse each stock price.
3. If the current price is smaller than `minPrice`:
   - Update `minPrice`.
4. Otherwise:
   - Calculate the profit:
     ```java
     currentProfit = price - minPrice
     ```
   - Update `maxProfit`.
5. Return `maxProfit`.

---

## Java Code

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice);
            }
        }

        return maxProfit;
    }
}
```

---

## Dry Run

### Input

```java
prices = [7,1,5,3,6,4]
```

### Initial Values

```
minPrice = ∞
maxProfit = 0
```

| Day | Price | minPrice | Profit | maxProfit |
|-----|------:|---------:|-------:|----------:|
| 1 | 7 | 7 | - | 0 |
| 2 | 1 | 1 | - | 0 |
| 3 | 5 | 1 | 4 | 4 |
| 4 | 3 | 1 | 2 | 4 |
| 5 | 6 | 1 | 5 | 5 |
| 6 | 4 | 1 | 3 | 5 |

Final Answer:

```java
5
```

---

## Why This Approach Works

At every step:

- `minPrice` stores the cheapest buying price seen so far.
- Selling at the current day's price gives the best possible profit for that day.
- `maxProfit` always stores the highest profit encountered.

This allows us to find the optimal answer in a single traversal.

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

The array is traversed only once.

---

### Space Complexity

```
O(1)
```

Only two extra variables (`minPrice` and `maxProfit`) are used.

---

## Edge Cases Considered

### Increasing Prices

```java
prices = [1,2,3,4,5]
```

Output:

```java
4
```

Buy on Day 1 and sell on Day 5.

---

### Decreasing Prices

```java
prices = [7,6,4,3,1]
```

Output:

```java
0
```

No profitable transaction is possible.

---

### Single Day

```java
prices = [5]
```

Output:

```java
0
```

Cannot sell after buying.

---

### Same Price Every Day

```java
prices = [3,3,3,3]
```

Output:

```java
0
```

No profit can be made.

---

### Lowest Price at the End

```java
prices = [5,4,3,2,1]
```

Output:

```java
0
```

Buying on the last day leaves no opportunity to sell.

---

### Lowest Price Before Highest Price

```java
prices = [8,2,6,1,9]
```

Output:

```java
8
```

Buy at **1** and sell at **9**.

---

## Pattern

- Array
- Greedy
- Single Traversal

---

## Key Takeaway

> The Greedy approach keeps track of the minimum stock price seen so far and continuously calculates the maximum possible profit. By scanning the array only once, it achieves an efficient solution with **O(n)** time complexity and **O(1)** space complexity.
