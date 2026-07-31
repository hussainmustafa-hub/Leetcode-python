# 169. Majority Element

Difficulty: Easy  
Topic: Array / Hash Table / Counting  
LeetCode Link: https://leetcode.com/problems/majority-element/

---

## Problem Description

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

---

## Solution Explanation

My algorithm uses a hash map (`count`) to keep track of the frequency of each number in the array:

1. I calculate `Limit = len(nums) // 2`, which represents the minimum frequency threshold a number must exceed to be considered the majority element.
2. I iterate through each number in `nums`:
   - If the number is already in `count`, I increment its tally by 1.
   - If it is not in `count`, I initialize its count to 1.
3. Immediately after updating the frequency, I check if `count[i] > Limit`. If it is, I return the current number `i` as the majority element.

---

## Complexity Analysis

- Time Complexity: O(n) — In the worst-case scenario, I iterate through the array of n numbers once, performing O(1) dictionary updates and lookups.
- Space Complexity: O(n) — I store up to n unique elements and their counts in the hash map.