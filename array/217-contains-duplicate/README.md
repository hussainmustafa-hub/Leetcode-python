# 217. Contains Duplicate

Difficulty: Easy  
Topic: Array / Hash Table / Set  
LeetCode Link: https://leetcode.com/problems/contains-duplicate/

---

## Problem Description

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Solution Explanation

My algorithm compares the total number of elements in the array to the number of unique elements:

1. I pass `nums` into Python's built-in `set()` to create a collection of unique elements (`new`).
2. A set automatically strips out any duplicate values.
3. I compare the length of the original `nums` list with the length of `new`:
   - If `len(nums) != len(new)`, it means duplicate values were present and removed, so I return `True`.
   - If the lengths are equal, all elements were unique, so I return `False`.

---

## Complexity Analysis

- Time Complexity: O(n) — Converting an array of n elements into a set takes linear time.
- Space Complexity: O(n) — In the worst-case scenario where all elements are distinct, the set stores up to n elements in memory.