# Modified Binary Search: Finding a Peak Element in an Unsorted Array
​
## Problem Statement
​
Given an unsorted array, find a peak element. A peak element is an element that is greater than its neighbors. The goal is to achieve this in **O(log n)** time using a modified Binary Search.
​
## Approach
​
### Key Insight
​
- A simple scan through the array can locate a peak in **O(n)** time, but this can be optimized using a modified Binary Search.
### Modified Binary Search
​
1. **Finding the Midpoint**:
- Start with `left` and `right` pointers at the beginning and end of the array.
- Calculate the `mid` index between `left` and `right`.
​
2. **Check Neighbors**:
- Compare the `mid` element with its left and right neighbors.
- If `mid` is not a peak (i.e., it has a greater neighbor), move in the direction of the greater neighbor. This guarantees the existence of a peak in that direction because there must be an increasing sequence leading to a peak.
​
3. **Adjust Pointers**:
- If the left neighbor is greater, move the `right` pointer to `mid - 1`.
- If the right neighbor is greater, move the `left` pointer to `mid + 1`.
​
4. **Repeat Until a Peak is Found**:
- The process continues until the pointers converge on a peak element.
​
## Why It Works
​
- By always moving towards the greater neighbor, we are guaranteed to find a peak because there cannot be an indefinitely increasing sequence in a finite array. This approach narrows down the search space logarithmically, achieving a time complexity of **O(log n)**.
​
## Summary
​
This modified Binary Search approach efficiently finds a peak element by leveraging the property that moving towards the greater neighbor ensures convergence to a peak. This method is significantly faster than a linear scan, reducing the time complexity to **O(log n)** while ensuring correctness.
​