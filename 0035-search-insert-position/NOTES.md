# Binary Search: Finding the Optimal Position
​
## Overview
​
Binary Search is an efficient algorithm for finding a target value within a sorted array. It repeatedly divides the search interval in half, narrowing down the potential locations of the target.
​
## Approach
​
1. **Initialize Pointers**:
- Set `left` to the start of the array and `right` to the end of the array.
​
2. **Iterate While `left` is Less Than or Equal to `right`**:
- Calculate the `mid` index as the average of `left` and `right`.
- If the middle element (`nums[mid]`) is less than the target, move `left` to `mid + 1`.
- If the middle element is greater than the target, move `right` to `mid - 1`.
- If the middle element equals the target, return `mid` as the target's index.
​
3. **Optimal Position**:
- If the target is not found, return `left` as it represents the best position to insert the target while maintaining order.
​
​