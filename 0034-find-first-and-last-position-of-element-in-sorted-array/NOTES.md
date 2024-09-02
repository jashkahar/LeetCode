# Finding the First and Last Position of an Element in a Sorted Array
​
## Problem Statement
​
Given a sorted array, find the first and last position of a target element. The goal is to achieve this in **O(log n)** time.
​
## Approach: Modified Binary Search with Left and Right Bias
​
### Key Insight
​
To efficiently find both the first and last positions of a target element, we can run Binary Search twice:
​
1. **Left Bias Binary Search**:
- This search is biased towards the left side. Even if the target is found, continue moving the pointer to the left to ensure finding the first occurrence of the element.
​
2. **Right Bias Binary Search**:
- This search is biased towards the right side. Even if the target is found, continue moving the pointer to the right to ensure finding the last occurrence of the element.
​
### Steps
​
1. **Run Left Bias Binary Search**:
- Initialize `left` and `right` pointers.
- Perform Binary Search, and when the target is found, adjust the `right` pointer to `mid - 1` to continue searching on the left side.
- This ensures the search moves left until the first occurrence is found.
​
2. **Run Right Bias Binary Search**:
- Reinitialize `left` and `right` pointers.
- Perform Binary Search, and when the target is found, adjust the `left` pointer to `mid + 1` to continue searching on the right side.
- This ensures the search moves right until the last occurrence is found.
​
3. **Return Positions**:
- After completing both searches, the indices from the left bias and right bias searches will indicate the first and last positions of the target.
​
## Why It Works
​
- By using two separate Binary Search runs with specific biases, the algorithm efficiently locates both boundaries of the target element in the sorted array.
- This approach ensures the overall time complexity remains **O(log n)**, leveraging the efficiency of Binary Search.
​
## Summary
​
This method involves running Binary Search twice with a left and right bias to find the first and last positions of a target element in a sorted array. By specifically adjusting pointers during each search, the algorithm accurately identifies the required positions in logarithmic time.
​