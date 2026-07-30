# 1. Two Sum

Difficulty: Easy  
Topic: Array / Hash Table  
LeetCode Link: https://leetcode.com/problems/two-sum/

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---

## Solution Explanation

My algorithm iterates through the array while maintaining a hash map (`seen`) to track elements and their corresponding indices:

1. For each number, I calculate `new_target = target - num`.
2. I check if `new_target` is already in the `seen` hash map:
   - If it exists, I return the index of `new_target` from the hash map along with the current index.
   - If it does not exist, I store the current `num` and its index in the hash map.


---

## Complexity Analysis

- Time Complexity: O(n) — I iterate through the array of n numbers at most once, performing O(1) dictionary lookups at each step.
- Space Complexity: O(n) — In the worst case, I store up to n elements in the dictionary.