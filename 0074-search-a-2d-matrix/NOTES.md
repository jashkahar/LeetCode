# Optimized Binary Search in a 2D Matrix
​
## Problem Statement
​
Given a 2D matrix where each row is sorted in ascending order, find a target value in the most optimal way. The goal is to achieve a time complexity of **O(log (n * m))**.
​
## Approach
​
1. **Binary Search to Identify the Correct Row**:
- Initialize `top` to the first row and `bottom` to the last row.
- Use Binary Search to find the row that could potentially contain the target:
- Check the rightmost value of the current row to determine if it's greater than or equal to the target (maximum boundary).
- Check the leftmost value of the current row to determine if it's less than or equal to the target (minimum boundary).
- Adjust `top` or `bottom` pointers accordingly to narrow down to the correct row.
​
2. **Binary Search within the Identified Row**:
- Once the correct row is found, perform a simple Binary Search within that row to find the target.
​
## Steps
​
1. **Find the Row**:
- While `top` is less than or equal to `bottom`, calculate the middle row.
- Compare the target with the values of the leftmost and rightmost elements of the middle row.
- Adjust `top` or `bottom` based on the comparisons.
​
2. **Search within the Row**:
- Perform a standard Binary Search on the identified row.