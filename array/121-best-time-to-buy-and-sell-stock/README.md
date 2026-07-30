# 121. Best Time to Buy and Sell Stock

Difficulty: Easy  
Topic: Array / Dynamic Programming / Sliding Window  
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

---

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## Solution Explanation

My algorithm keeps track of two variables as it iterates through the stock prices:
1. `min_price`: The lowest price seen so far.
2. `max_profit`: The maximum profit calculated so far.

For each price in the array:
- If the current price is less than `min_price`, I update `min_price` because buying at a lower price allows for potentially higher profit in the future.
- Otherwise, I calculate the potential profit (`current price - min_price`) and update `max_profit` if it exceeds my previous maximum.

---

## Complexity Analysis

- Time Complexity: O(n) — I iterate through the array of n prices exactly once.
- Space Complexity: O(1) — I only store a few variables (`min_price`, `max_profit`, `profit`), using constant extra memory.