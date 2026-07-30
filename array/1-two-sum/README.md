First LeetCode Problem.Attempted 10 Times

⏱️ Time Complexity: O(n)
💾 Space Complexity: O(n)

approach:
    Instead of looping through the whole list and comparing every number with every other number(which i did before) which was highly inefficient(Time Complexity: O(n*n) and Space Complexity: O(1)).I Subtracted the number from the target then checked(using seen={}Dict) if i have seem the answer before.