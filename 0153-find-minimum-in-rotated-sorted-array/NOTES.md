# Finding the Minimum in a Rotated Sorted Array
​
## Problem Statement
​
Given a rotated sorted array, find the minimum element in the array. The solution must run in **O(log n)** time.
​
## Approach: Modified Binary Search
​
### Key Insight
​
To efficiently find the minimum element in a rotated sorted array, a modified Binary Search is required due to the rotation. The approach involves narrowing down the search space by eliminating halves of the array that do not contain the minimum.
​
### Modified Binary Search Steps
​
1. **Compute the Midpoint**:
- Start with `left` and `right` pointers at the beginning and end of the array.
- Calculate the `mid` index between `left` and `right`.
​
2. **Determine the Search Direction**:
- If `mid` is greater than the value at `left`, the left half is sorted, and the minimum is not in this half. Thus, eliminate the left half by moving the `left` pointer to `mid + 1` and continue searching the right side.
- If `mid` is less than or equal to the value at `right`, then the right half is sorted, and the minimum must be in the left part. Move the `right` pointer to `mid` to continue searching the left side.
​
3. **Handling Fully Sorted Half**:
- If the `mid` element is greater than the `left` element, it indicates the current half is fully sorted. In this case, update the minimum value to be the smaller of the current minimum and the value at `left`.
​
4. **Continue Until Minimum is Found**:
- Repeat the steps until `left` and `right` pointers converge on the minimum element.
​
## Why It Works
​
- By leveraging the sorted properties of the halves, this approach systematically eliminates the half that cannot contain the minimum, maintaining the logarithmic time complexity.
- The algorithm efficiently narrows down the search space while ensuring the correct minimum value is identified by comparing midpoints and adjusting pointers accordingly.
​
## Summary
​
This modified Binary Search approach identifies the minimum element in a rotated sorted array by repeatedly comparing midpoints and eliminating the unnecessary halves. The algorithm maintains a time complexity of **O(log n)** by exploiting the sorted properties of subarrays and efficiently narrowing down the search space.
​